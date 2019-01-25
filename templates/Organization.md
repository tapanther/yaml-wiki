{% extends 'base.md' -%}

{%- block title %}
{{ title }}
{% endblock %}

{%- block summary %}
Main Page for {{ title }}
{% endblock %}

{%- block pagecontent %}
{% if Structure %}
## Structure

{% if Structure.Governance %}
### Governnance

{{ Structure.Governance | autoLink }}

{% endif %}{# Governance #}
{% if Structure.Locations %}
### Notable Locations

{{ macros.dictList(Structure.Locations) }}

{% endif %}{# Locations #}
{% if Structure.Members %}
### Notable Members

{{ macros.dictList(Structure.Members) }}

{% endif %}{# Members #}
{% if Structure.Associations %}
### Organization Associations

{{ macros.dictSection(Structure.Associations) }}

{% endif %}{# Associations #}
{% endif %}{# Structure #}
{% if Culture %}
## Culture

{{ Culture.Description | autoLink }}

{% if Culture.Values %}
### Values

{% for value in Culture.Values %}
- {{ value }}
{% endfor %}
{% endif %}{# Values #}
{% if Culture.Traditions %}
### Traditions

{{ macros.dictList(Culture.Traditions) }}

{% endif %}{# Traditions #}
{% endif %}{# Culture #}
{% endblock %}
