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

{{ Society.Diagrams.Government }}

{% endif %}

{{ Society.Government | autoLink }}

{% endif %}{# Government #}
{% if Society.Locations %}
### Notable Locations

{% filter autoLink %}
{{ macros.dictList(Society.Locations) }}
{% endfilter %}

{% endif %}{# Locations #}
{% if Society.Organizations %}
### Prominent Figures and Organizations

{% filter autoLink %}
{{ macros.dictSection(Society.Organizations) }}
{% endfilter %}

{% endif %}{# Organizations #}
{% endif %}{# Society #}
{% if Culture %}
## Culture

{{ Culture.Description | autoLink }}

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

{{ Culture.Religion|autoLink }}

{% endif %}{# Religion #}
{% if Culture.Traditions %}
### Traditions

{% filter autoLink %}
{{ macros.dictList(Culture.Traditions) }}
{% endfilter %}

{% endif %}{# Traditions #}
{% if Culture.Heroes or Culture.Villains %}
### Heroes & Villains

{% filter autoLink %}
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
