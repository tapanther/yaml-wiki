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
{% if Content[0].separate %}

---

{% endif %}{# Description Separate #}
{% endif %}{# Description#}
{% for entry in Content %}
{% if entry.Title %}
## {{ entry.Title }}

{% endif %}
{% if entry.Subtitle %}
*{{ entry.Subtitle }}*

{% endif %}{# Subtitle #}
{% if entry.Text %}
{{ entry.Text | autoLink }}
{% endif %}
{% if entry.separate and not loop.last %}

---

{% endif %}{# separate #}
{% endfor %}{# Content #}
{% endblock %}