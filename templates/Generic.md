{% extends 'base.md' -%}

{%- block title %}
{{ title }}
{% endblock %}

{%- block summary %}
Main Page for {{ title }}
{% endblock %}

{%- block pagecontent %}
{% if GeneralInfo and GeneralInfo.Description and Content[0].separate %}

---

{% endif %}{# Description Separate #}
{% for entry in Content %}
{% if entry.separate and not loop.first %}

---

{% endif %}{# separate #}
{% if entry.Title %}
## {{ entry.Title }}

{% endif %}
{% if entry.Subtitle %}
{% if (control and 'subtitle_headings' in control) or entry.subtitle_heading %}
### {{ entry.Subtitle }}
{% else %}
*{{ entry.Subtitle }}*
{% endif %}

{% endif %}{# Subtitle #}
{% if entry.Diagram %}

{{ entry.Diagram }}

{% endif %}{# Diagram #}
{% if entry.Text %}

{{ entry.Text | auto_link }}

{% endif %}
{% if entry.Table %}
{% if entry.Table.Meta %}
{% set indent_w = 4 if entry.Table.Meta.Admonition else 0 %}
{% if entry.Table.Meta.Admonition %}
{{ "???" if entry.Table.Meta.Admonition.Collapse else "!!!"}} {{ entry.Table.Meta.Admonition.Type }} "{{ entry.Table.Meta.Admonition.Title }}"

{% endif %}
{% filter indent(indent_w, first=True) %}

|{% for col in entry.Table.Meta.Columns %} {{ col }} |{% endfor %}

|{% for col in entry.Table.Meta.Columns %}{% if not loop.last %}:---:|{% else %}:---|{% endif %}{% endfor %}

{% for resultArr in entry.Table.Meta.Rows %}
|{% for txt in resultArr %} {{ txt }} |{% endfor %}

{% endfor %}
{% endfilter %}
{% else %}

| Roll | Result |
|:----:|:-------|
{% for roll, result in entry.Table|roll_sort %}
| {{roll}} | {{result}} |
{% endfor %}

{% endif %}
{% endif %}{# Table #}

{% endfor %}{# Content #}
{% endblock %}
