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

{% filter autoLink %}
{{ macros.dictList(Geography.Features) }}
{% endfilter %}

{% endif %}{# Features #}
{% if Geography.Settlements %}
### Notable Settlements

{% filter autoLink %}
{{ macros.dictSection(Geography.Settlements) }}
{% endfilter %}

{% endif %}{# Settlements #}
{% endif %}{# Geography #}
{% endblock %}
