{% extends 'base.md' %}

{% set title = 'Tritan' %}

{% block title %}
{{ title }}
{% endblock %}

{% block summary %}
Main Page
{% endblock %}

{% block general_information %}
{% endblock %}

{% block pagecontent %}

## Using this Site

Use the navigation bar to explore the different aspects of Tritan.


You can alternatively use the category pages below to narrow your
scope, or use the search bar at the top to find a specific page.

## Category Pages

{% for child in navTree.children | sort(attribute='name') %}
- [{{ child.name }}]({{ child.file }})
{% endfor %}

{% endblock pagecontent %}