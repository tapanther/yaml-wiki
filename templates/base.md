---
title: {% block title %}{% endblock %}
summary: {% block summary %}{% endblock %}
authors: Juan P. Sierra
date: {{ date }}
---


{% import 'macros.md' as macros %}

# {{ title | title }}

{% block pagecontent %}{% endblock %}