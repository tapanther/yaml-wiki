{% extends 'base.md' %}

{% block title %}
Tritan
{% endblock %}

{% block summary %}
Main Page
{% endblock %}

{% block general_information %}
{% endblock %}

{% block pagecontent %}

## Using this Site

Use the navigation bar to explore the different aspects of Tritan.

## Quick Links

{% for category, data in navStruct | dictsort %}
*********
**{{ category }}**

{% for item in (data | sort(attribute='title')) if not item.noLink %}
- [{{ item.title }}][]
{% endfor %}

{% endfor %}

{% endblock pagecontent %}