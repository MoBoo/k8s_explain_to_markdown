# K8s kubectl explain exporter
Script to recursively export 'kubectl explain <resource>' commands to markdown.
# Usage
```
usage: main.py [-h] [-t TEMPLATE_NAME] [-d TEMPLATE_DIR] [-o OUTPUT] resource

positional arguments:
  resource              the k8s resource to pull explanations for.

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATE_NAME, --template_name TEMPLATE_NAME
                        template file to use for generating output.
  -d TEMPLATE_DIR, --template_dir TEMPLATE_DIR
                        directory path where templates are located.
  -o OUTPUT, --output OUTPUT
                        output file path to store rendered output in. Defaults
                        to <resource>.md
```
# Example Usage
```
python3 main.py deployment # default
python3 main.py service -t custom_template.md -d /path/to/custom/template_directory
```

# Example Output
[Deployment.md](deployment.md)

# Improvements
- Add support for multiple output formats, making use of the `-o, --output` parameter.
