{% extends 'base.md' -%}

{%- block title %}
{{ title }}
{% endblock %}

{%- block summary %}
Main Page for {{ title }}
{% endblock %}

{%- block pagecontent %}
{% if Geography %}
## Geography

{% if Geography.Description %}
{{ Geography.Description | autoLink }}

{% endif %}{# Description #}
{% if Geography.Features %}
### Notable Featires

{{ macros.dictList(Geography.Features) }}

{% endif %}{# Features #}
{% if Geography.Settlements %}
### Notable Settlements

{{ macros.dictSection(Geography.Settlements) }}

{% endif %}{# Settlements #}
{% endif %}{# Geography #}
{% endblock %}
