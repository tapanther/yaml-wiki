{% extends 'base.md' -%}

{%- block title %}
{{ title }}
{% endblock %}

{%- block summary %}
Main Page for {{ title }}
{% endblock %}

{%- block pagecontent %}
## General Info

- Type : {{ GeneralInfo.Type }}
- Region : {{ GeneralInfo.Region }}
- Population : {{ GeneralInfo.Population | numberFormat }}

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
