
{% macro dictSection(dict) %}
{% for name, desc in dict.items() %}
**{{ name }}**

{{ desc }}

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

    {{ desc|listText }}
    
{% endfor %}
{% endmacro %}
