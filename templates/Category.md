{% extends 'base.md' -%}

{% set title = navTree.name %}

{%- block title %}
{{ title }}
{% endblock %}

{% block pagetitle %}
# {{ title }}

-----

{% endblock %}{# pagetitle #}

{%- block summary %}
Main Page for {{ title }}
{% endblock %}

{% block pagecontent %}
## Uncategorized
{% for child in navTree|get_tree_direct_children if not child.noLink %}
{{ macros.printCatLinks(child, 0) }}
{%- endfor %}
{% endblock %}
