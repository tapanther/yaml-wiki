{% extends 'base.md' -%}

{%- block title %}
{{ title }}
{% endblock %}

{%- block summary %}
Main Page for {{ title }}
{% endblock %}

{%- block pagecontent %}
{% if Society %}
## Society

{% if Society.Government %}
### Government
{% if Society.Diagrams and Society.Diagrams.Government %}

{{ Society.Diagrams.Government|relative_link }}

{% endif %}

{{ Society.Government | auto_link }}

{% endif %}{# Government #}
{% if Society.Locations %}
### Notable Locations

{% filter auto_link %}
{{ macros.dictList(Society.Locations) }}
{% endfilter %}

{% endif %}{# Locations #}
{% if Society.Organizations %}
### Prominent Figures and Organizations

{% filter auto_link %}
{{ macros.dictSection(Society.Organizations) }}
{% endfilter %}

{% endif %}{# Organizations #}
{% endif %}{# Society #}
{% if Culture %}
## Culture

{{ Culture.Description | auto_link }}

{% if Culture.CoreBeliefs %}
### Core Beliefs

{% for belief in Culture.CoreBeliefs %}
- **{{ belief }}**
{% endfor %}
{% endif %}{# Core Beliefs #}
{% if Culture.Values %}
### Values

{% for value in Culture.Values %}
- {{ value }}
{% endfor %}
{% endif %}{# Values #}
{% if Culture.Prejudices %}
### Prejudices

{% for prej in Culture.Prejudices %}
- {{ prej }}
{% endfor %}
{% endif %}{# Prejudices #}
{% if Culture.Religion %}
### Religion

{{ Culture.Religion|auto_link }}

{% endif %}{# Religion #}
{% if Culture.Traditions %}
### Traditions

{% filter auto_link %}
{{ macros.dictList(Culture.Traditions) }}
{% endfilter %}

{% endif %}{# Traditions #}
{% if Culture.Heroes or Culture.Villains %}
### Heroes & Villains

{% filter auto_link %}
{% if Culture.Heroes %}
#### Heroes

{{ macros.dictList(Culture.Heroes) }}

{% endif %}{# Heroes #}
{% if Culture.Villains %}
#### Villains

{{ macros.dictList(Culture.Villains) }}

{% endif %}{# Villains #}
{% endfilter %}
{% endif %}{# Heroes or Villains #}
{% endif %}{# Culture #}
{% endblock %}
