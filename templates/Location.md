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
{{ Geography.Description | auto_link }}

{% endif %}{# Description #}
{% if Geography.Features %}
### Notable Featires

{% filter auto_link %}
{{ macros.dictList(Geography.Features) }}
{% endfilter %}

{% endif %}{# Features #}
{% if Geography.Settlements %}
### Notable Settlements

{% filter auto_link %}
{{ macros.dictSection(Geography.Settlements) }}
{% endfilter %}

{% endif %}{# Settlements #}
{% endif %}{# Geography #}
{% endblock %}
