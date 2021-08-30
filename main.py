import subprocess
from jinja2 import Environment as Jinja_Environment, FileSystemLoader as Jinja_FSLoader, select_autoescape
import logging

NESTED_FIELD_TYPES = ("Object", "[]Object")
KUBECTL_BASE_CMD = ["kubectl", "explain"]
KUBECTL_NESTED_DESCRIPTION = "     "


class Field:
    class Metadata:
        def __init__(self, kind=None, version=None, desc=None):
            self.kind = kind
            self.version = version
            self.desc = desc

    def __init__(self, field_name, field_type, field_desc, field_required=False, kind=None, version=None, desc=None,
                 parent=None):
        self.name = field_name

        # remove '<' and '>' from type
        self.type = field_type[1:-1] if field_type and field_type.startswith("<") else field_type

        self.desc = field_desc
        self.is_required = field_required
        self.parent = parent

        self.metadata = Field.Metadata(kind, version, desc)
        self.fields = list()

    def resolve_resource_path(self):
        if self.parent:
            return f"{self.parent.resolve_resource_path()}.{self.name}"
        else:
            return self.metadata.kind

    def add_field(self, field):
        self.fields.append(field)

    def __str__(self):
        if self.parent:
            return f"{self.parent.resolve_resource_path()}{'.' if self.parent else ''}{self.name} <{self.type}> {'-required-' if self.is_required else ''}: {self.desc}"
        else:  # it's a top-level resource
            return f"{self.name} <{self.type}>: {self.desc}"

    def __repr__(self):
        if self.parent:
            return f"Field({self.name}, {self.type}, {self.desc} {', True' if self.is_required else ''}, {self.metadata!s}, {self.parent})"
        else:
            return f"Field({self.name}, {self.type}, {self.desc})"


def get_output(cmd: list):
    """
    Uses the 'subprocess'-module to execute the 'kubectl explain <resource>' command and return the stdout-ouput as a string.
    Even tho this works for any command, the hole idea of this code it to run the kubectl command.

    :param cmd: command to execute in list format, eg. ["kubectl", "explain", "<resource>"]
    :return: stdout-output of kubectl command
    """
    logging.debug(f"retreiveing output for cmd: {' '.join(cmd)}")
    if isinstance(cmd, str):
        cmd = cmd.split(" ")

    rv = subprocess.run(cmd, capture_output=True)
    if rv.returncode:
        raise ConnectionRefusedError(rv.stderr.decode())
    return rv.stdout.decode()


def parse_output(output: str, parent=Field(None, None, None)):
    """
    Takes the output of the 'kubectl explain <resource>' command as a string and recursively parses it to a tree-structure of fields,
    with the corresponding metadata and child-fields.

    :param output: output of the 'kubectl explain <resource>' command. (Usually received via the 'get_output' function)
    :param parent: optional, parent-field-obj to which subfields are queried. (used to back-link child-objs with their parent) (used to resolve a childs full resource path, eg. deployment.metadata.name)
    :return: root obj of the field tree-structure (normally top-level resource like 'deployment', 'service, etc.)
    """
    logging.debug(f"parsing output")
    metadata, fields = output.split("FIELDS:")

    logging.debug(f"parsing metadatafor {parent.name}")
    metadata = [line.strip() for line in metadata.split("\n") if line.strip()]
    for _, line in enumerate(metadata):
        if line != 'DESCRIPTION:':
            key, value = line.split(":")
            setattr(parent.metadata, key.strip().lower(), value.strip())
        else:  # if line == 'DESCRIPTION:'
            parent.metadata.desc = ' '.join([line.strip() for line in metadata[_ + 1:]])
            break

    logging.debug(f"parsing fields for {parent.name}")
    fields = [line for line in fields.split("\n\n") if line.strip()]
    fields = merge_descriptions(fields)
    for field in fields:
        field, *desc = field.split("\n")

        field_desc = ' '.join([line.strip() for line in desc])

        field_name, field_type = field.split("\t")
        field_required = False
        if not field_type.endswith(">"):
            field_type = field_type.split(" ")[0]
            field_required = True

        field = Field(field_name, field_type, field_desc, field_required, parent=parent)
        if field.type in NESTED_FIELD_TYPES:
            cmd = KUBECTL_BASE_CMD.copy()
            cmd.append(field.resolve_resource_path())
            field = parse_output(get_output(cmd), parent=field)

        parent.add_field(field)

    return parent


def merge_descriptions(fields: list):
    """
    Some Field descriptions have an additional paragraph seperated by a newline.
    this seperate paragraph needs to be merged with the field description to allow for correct further processing.

    :param fields: List of the fields of a resource
    :return: list of fields with merged descriptions
    """
    logging.debug(f"merging field descriptions")
    new_fields_list = list()
    for line in fields:
        if line.startswith(KUBECTL_NESTED_DESCRIPTION):
            new_fields_list[-1] = f"{new_fields_list[-1]} {line}"
        else:
            new_fields_list.append(line.strip())

    return new_fields_list


def render_doc(root_obj: Field, template_name: str, template_dir: str, output: str):
    """
    Renders the field tree-structure from 'parse_output' into a markdown file using jinj2 as a render-engine.

    :param root_obj:
    :param template_name: name of the template file to use. Assuming it's in the template directory.
    :param output: filepath of the output file.
    :return: None
    """
    logging.debug(f"rendering to markdown")
    jinja_env = Jinja_Environment(loader=Jinja_FSLoader(template_dir), autoescape=select_autoescape())
    template = jinja_env.get_template(template_name)
    template.stream(resource=root_obj).dump(f"{output}.{template_name.split('.')[-1]}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("resource", help="the k8s resource to pull explanations for.", action="store")
    parser.add_argument("-t", "--template_name", action="store", dest="template_name", required=False,
                        default="template.md", help="template file to use for generating output.")
    parser.add_argument("-d", "--template_dir", action="store", dest="template_dir", required=False, default="template",
                        help="directory path where templates are located.")
    parser.add_argument("-o", "--output", action="store", dest="output", required=False,
                        help="output file path to store rendered output in. Defaults to <resource>.<template_ext>")

    args = parser.parse_args()

    cmd = KUBECTL_BASE_CMD.copy()
    cmd.append(args.resource)

    rv = parse_output(get_output(cmd), parent=Field(args.resource, None, None))
    render_doc(rv, args.template_name, args.template_dir, args.output if args.output else args.resource)
