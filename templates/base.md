---
title: {% block title %}{% endblock %}
summary: {% block summary %}{% endblock %}
authors: Juan P. Sierra
date: {{ date }}
{% block addMeta %}{% endblock %}
---
{% import 'macros.md' as macros with context %}

{% block pagetitle %}
# {{ title | title }}

-----

{% endblock %}{# pagetitle #}

{% block generalinformation %}
{% if GeneralInfo %}
{% if GeneralInfo.Statistics or GeneralInfo.Ethics or GeneralInfo.Ethics %}
## General Info

{% endif %}{# GeneralInfo Header #}
{% if GeneralInfo.Statistics %}
{% for stat, data in GeneralInfo.Statistics | dictsort %}
- {{ stat | capitalize }} : {{ data | numberFormat }}
{% endfor %}
{% endif %}{# Statistics #}
{% if GeneralInfo.Ethics %}
- Ethics:
{% for ethic in GeneralInfo.Ethics %}
    - {{ ethic }}
{% endfor %}
{% endif %}{# Ethics #}
{% if GeneralInfo.Traits %}
- Traits:
{% for trait in GeneralInfo.Traits %}
    - {{ trait }}
{% endfor %}
{% endif %}{# Traits #}
{% if GeneralInfo.Description %}
### Description

{{ GeneralInfo.Description | autoLink }}

{% endif %}{# Description #}
{% endif %}{# GeneralInfo #}
{% endblock generalinformation %}

{% block pagecontent %}
{% endblock %}

{% block timeline %}
{% if History %}
## History

{% if History.Description %}
### Historical Account

{{ History.Description | autoLink }}
{% endif %}{# Description #}
{% if History.Timeline %}
### Timeline

Date | Name | Event
:---:|:----:|:----
{% for event in History.Timeline %}
{{ event.Date }} | {{ event.Name }} | {{ event.Description }}
{% endfor %}
{% endif %}{# History #}
{% endif %}{# History #}

{% endblock %}{# Timeline #}

{% block pagelinks %}
{% if Links %}
## Related Links

{% for link in Links %}
- [{{ link }}][]
{% endfor %}
{% endif %}{# Links #}
{% endblock %}

{% block pageRefs %}
{% if Refs %}
{% for ref, link in Refs|dictsort %}
[{{ ref }}]: {{ link }}
{% endfor %}
{% endif %}{# Refs #}
{% endblock %}

{% include 'links.md.j2' %}
