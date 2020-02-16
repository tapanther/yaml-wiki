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
{% if Structure.Diagrams and Structure.Diagrams.Governance %}

{{ Structure.Diagrams.Governance }}

{% endif %}{# GovDiagram #}

{{ Structure.Governance | autoLink }}

{% endif %}{# Governance #}
{% if Structure.Locations %}
### Notable Locations

{% filter autoLink %}
{{ macros.dictList(Structure.Locations) }}
{% endfilter %}

{% endif %}{# Locations #}
{% if Structure.Members %}
### Notable Members

{% filter autoLink %}
{{ macros.dictList(Structure.Members) }}
{% endfilter %}

{% endif %}{# Members #}
{% if Structure.Associations %}
### Organization Associations

{% filter autoLink %}
{{ macros.dictSection(Structure.Associations) }}
{% endfilter %}

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
