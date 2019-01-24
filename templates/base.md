---
title: {% block title %}{% endblock %}
summary: {% block summary %}{% endblock %}
authors: Juan P. Sierra
date: {{ date }}
{% block addMeta %}{% endblock %}
---
{% import 'macros.md' as macros with context %}

# {{ title | title }}

{% block pagecontent %}{% endblock %}

{% block timeline %}
{% if History %}
## History

### Timeline

Date | Name | Event
:---:|:----:|:----
{% for event in History.Timeline %}
{{ event.Date }} | {{ event.Name }} | {{ event.Description }}
{% endfor %}
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

{% include 'links.md.j2' %}