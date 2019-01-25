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

{% for child in navTree.children | sort(attribute='name') %}
{{ macros.printTreeLinks(child, 0) }}
{% endfor %}

{% endblock pagecontent %}