{% extends 'base.md' %}

{% block title %}
{{ mkdocs_yaml.site_name }}
{% endblock %}

{% block summary %}
Main Page
{% endblock %}

{% block general_information %}
{% endblock %}

{% block pagecontent %}

## Using this Site

{% if not mkdocs_yaml.index_tag_text %}
Use the navigation bar to explore the different aspects of {{ mkdocs_yaml.site_name }}.


You can alternatively use the category pages below to narrow your
scope, or use the search bar at the top to find a specific page.
{% else %}

{{ mkdocs_yaml.index_tag_text }}

{% endif %}

## Category Pages

{% for child in navTree.children | sort(attribute='name') %}
- [{{ child.name }}]({{ child.file }})
{% endfor %}

{% endblock pagecontent %}