{% extends 'base.md' -%}

{%- block title %}
{{ title }}
{% endblock %}

{%- block summary %}
Main Page for {{ title }}
{% endblock %}

{%- block pagecontent %}
{% if Description %}
{{ Description }}
{% if Content[0].separate %}

---

{% endif %}{# Description Separate #}
{% endif %}{# Description#}
{% for entry in Content %}
## {{ entry.Title }}
{% if entry.Subtitle %}
*{{ entry.Subtitle }}*

{% endif %}{# Subtitle #}
{{ entry.Text }}
{% if entry.separate and not loop.last %}

---

{% endif %}{# separate #}
{% endfor %}{# Content #}
{% endblock %}