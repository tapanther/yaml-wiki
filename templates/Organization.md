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
- Membership : {{ GeneralInfo.Membership | numberFormat }}
- Allegiance : {{ GeneralInfo.Allegiance }}

{% if GeneralInfo.Description %}
{{ GeneralInfo.Description }}
{% endif %}{# Description #}
{% if Structure %}
## Structure

{% if Structure.Governance %}
### Governnance

{{ Structure.Governance }}

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

{{ Culture.Description }}

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
{% if History %}
## History

### Timeline

Date | Name | Event
:---:|:----:|:----
{% for event in History.Timeline %}
{{ event.Date }} | {{ event.Name }} | {{ event.Description }}
{% endfor %}
{% endif %}{# History #}

{% endblock %}
