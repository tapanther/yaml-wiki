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

{% include 'links.md.j2' %}