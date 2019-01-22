{% extends 'base.md' %}

{% block title %}
Tritan
{% endblock %}

{% block summary %}
Main Page
{% endblock %}

{% block pagecontent %}

## Using this Site

Use the navigation bar to explore the different aspects of Tritan.

## Quick Links

{% for category, data in navStruct|dictsort %}
*********
**{{ category }}**

{% for item in data|sort(attribute='title') %}
- [{{ item.title }}][]
{% endfor %}

{% endfor %}

{% endblock pagecontent %}