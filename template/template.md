# {{ resource.resolve_resource_path() }}

---

{% if resource.type %}**Type**: {{ resource.type }}{% endif %}{% if resource.is_required %} (required){% endif %}

## Description
{{ resource.desc or resource.metadata.desc }}

{% if resource.kind or resource.version %}
## Metadata
**Kind**: {{ resource.metadata.kind }}

**Version**: {{ resource.metadata.version }}

{% if resource.type %} **type**: <{{ resource.type }}> {% endif %}
{% endif %}

{% if resource.fields %}
## Fields
{% for resource in resource.fields %}
<details>
<summary>{{ resource.name }}{% if resource.type %}: {{ resource.type }}{% endif %}{% if resource.is_required %} required!{% endif %}</summary>

{% include 'template.md' %}

</details>
{% endfor %}
{% endif %}

---