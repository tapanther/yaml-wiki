{% macro printTreeYAML(tree, level) %}
{% if tree.children %}
{{ ( '- ' + tree.name ) | indent(2*level, true) }} :
{% for child in tree.children | sort(attribute='name') if not child.noLink %}
{{ printTreeYAML(child, level+1 ) }}
{%- endfor %}
{% else %}
{{ ('- ' + tree.name ) | indent(2*level, true) }} : {{ tree.file }}
{% endif %}
{% endmacro %}


{% macro printTreeLinks(tree, level) %}
{% set cats = [] %}
{% if tree.children %}
{% do cats.append(tree) %}
{% else %}
{{ ('- [' + tree.name + '][]') | indent(4*level, true) }}
{% endif %}
{% for cat in cats %}
{{ ( '- **' + cat.name + '**') | indent(4*level, true) }}
{% for child in cat.children | sort(attribute='name') if not child.noLink %}
{{ printTreeLinks(child, level+1 ) }}
{%- endfor %}
{%- endfor %}
{% endmacro %}


{% macro printCatLinks(tree, level) %}
{% if tree.children %}
{{ '#' * (level + 2) }}  {{ tree.name }}

{% for child in tree.children | sort(attribute='name') if not child.noLink %}
{{ printCatLinks(child, level+1 ) }}
{%- endfor %}
{% else %}
- [{{ tree.name }}][]
{% endif %}
{% endmacro %}



{% macro dictSection(dict) %}
{% for name, desc in dict.items() %}
**{{ name }}**

{{ desc | autoLink }}

{% endfor %}
{% endmacro %}

{% macro dictTable(dict) %}
{% for name, desc in dict.items() %}
| {{ name }} | {{ desc }} |
{% endfor %}
{% endmacro %}

{% macro dictList(dict) %}
{% for name, desc in dict.items() %}
- *{{ name }}* :

    {{ desc|autoLink|listText }}
    
{% endfor %}
{% endmacro %}
