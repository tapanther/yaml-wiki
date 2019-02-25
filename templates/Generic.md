{% extends 'base.md' -%}

{%- block title %}
{{ title }}
{% endblock %}

{%- block summary %}
Main Page for {{ title }}
{% endblock %}

{%- block pagecontent %}
{% if Description %}

{{ Description | autoLink }}

{% endif %}{# Description#}
{% for entry in Content %}
{% if entry.separate and not loop.first %}

---

{% endif %}{# separate #}
{% if entry.Title %}
## {{ entry.Title }}

{% endif %}
{% if entry.Subtitle %}
*{{ entry.Subtitle }}*

{% endif %}{# Subtitle #}
{% if entry.Text %}

{{ entry.Text | autoLink }}

{% endif %}
{% if entry.Table %}
{% if entry.Table.Meta and entry.Table.Meta.Columns %}

|{% for col in entry.Table.Meta.Columns %} {{ col }} |{% endfor %}

|{% for col in entry.Table.Meta.Columns %}{% if not loop.last %}:---:|{% else %}:---|{% endif %}{% endfor %}

{% for entry, resultArr in entry.Table.Rows.items() %}
| {{ entry }} |{% for txt in resultArr %} {{ txt }} |{% endfor %}

{% endfor %}
{% else %}

| Roll | Result |
|:----:|:-------|
{% for roll, result in entry.Table|dictsort %}
| {{roll}} | {{result}} |
{% endfor %}

{% endif %}
{% endif %}
{% endfor %}{# Content #}
{% endblock %}
