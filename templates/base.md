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

{% block image %}
{{ Image }}
{% endblock %}

{% block generalinformation %}
{% if GeneralInfo %}
{% if GeneralInfo.Statistics or GeneralInfo.Ethics or GeneralInfo.Ethics %}
## General Info

{% endif %}{# GeneralInfo Header #}
{% if GeneralInfo.Statistics %}
{% for stat, data in GeneralInfo.Statistics | dictsort %}
- {{ stat | capitalize }} : {{ data | number_format }}
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
{% if GeneralInfo.AddInfo %}
{% for blk_name, blk_info in GeneralInfo.AddInfo|dictsort %}

### {{ blk_name }}

{% if blk_info is mapping %}
{% for stat, data in blk_info|dictsort %}
  - {{ stat | capitalize }} : {{ data | number_format }}
{% endfor %}
{% elif blk_info is iterable %}
{% for datum in blk_info %}
  - {{ datum }}
{% endfor %}
{% else %}
    {{ blk_info }}
{% endif %}
{% endfor %}
{% endif %}{# AddInfo #}
{% if GeneralInfo.Diagram %}

{{ GeneralInfo.Diagram|relative_link }}

{% endif %}{# Diagram #}
{% if GeneralInfo.Description %}
### Description

{{ GeneralInfo.Description | auto_link }}

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

{{ History.Description | auto_link }}
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
{% if link.startswith('[') %}
- {{ link }}
{% else %}
- [{{ link }}][]
{% endif %}
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
