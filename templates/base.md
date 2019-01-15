---
title: {% block title %}{% endblock %}
summary: {% block summary %}{% endblock %}
authors: Juan P. Sierra
date: {{ date }}
{% block addMeta %}{% endblock %}
---
{% import 'macros.md' as macros %}

# {{ title | title }}

{% block pagecontent %}{% endblock %}

{% block pagelinks %}
{% if Links %}
## Related Links

{% for link in Links %}
- [{{ link }}][]
{% endfor %}
{% endif %}{# Links #}
{% endblock %}

{% include 'links.md.j2' %}