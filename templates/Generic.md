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
{% if control and 'subtitle_headings' in control %}
### {{ entry.Subtitle }}
{% else %}
*{{ entry.Subtitle }}*
{% endif %}

{% endif %}{# Subtitle #}
{% if entry.Text %}

{{ entry.Text | autoLink }}

{% endif %}
{% if entry.Table %}
{% if entry.Table.Meta %}

|{% for col in entry.Table.Meta.Columns %} {{ col }} |{% endfor %}

|{% for col in entry.Table.Meta.Columns %}{% if not loop.last %}:---:|{% else %}:---|{% endif %}{% endfor %}

{% for resultArr in entry.Table.Meta.Rows %}
|{% for txt in resultArr %} {{ txt }} |{% endfor %}

{% endfor %}
{% else %}

| Roll | Result |
|:----:|:-------|
{% for roll, result in entry.Table|rollSort %}
| {{roll}} | {{result}} |
{% endfor %}

{% endif %}
{% endif %}{# Table #}

{% endfor %}{# Content #}
{% endblock %}