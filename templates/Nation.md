{% extends 'base.md' -%}

{%- block title %}
{{ title }}
{% endblock %}

{%- block summary %}
Main Page for {{ title }}
{% endblock %}

{%- block pagecontent %}
## General Info

- Population : {{ GeneralInfo.Population | numberFormat }}
- Government : {{ GeneralInfo.Government }}
- Ethics :
{% for ethic in GeneralInfo.Ethics %}
    - {{ ethic }}
{% endfor %}

{% if Society %}
## Society

{% if Society.Government %}
### Government

{{ Society.Government }}

{% endif %}{# Government #}
{% if Society.Locations %}
### Notable Locations

{{ macros.dictList(Society.Locations) }}

{% endif %}{# Locations #}
{% if Society.Organizations %}
### Prominent Figures and Organizations

{{ macros.dictSection(Society.Organizations) }}

{% endif %}{# Organizations #}
{% endif %}{# Society #}
{% if Culture %}
## Culture

{{ Culture.Description }}

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

{{ Culture.Religion }}

{% endif %}{# Religion #}
{% if Culture.Traditions %}
### Traditions

{{ macros.dictList(Culture.Traditions) }}

{% endif %}{# Traditions #}
{% if Culture.Heroes or Culture.Villains %}
### Heroes & Villains

{% if Culture.Heroes %}
#### Heroes

{{ macros.dictList(Culture.Heroes) }}

{% endif %}{# Heroes #}
{% if Culture.Villains %}
#### Villains

{{ macros.dictList(Culture.Villains) }}

{% endif %}{# Villains #}
{% endif %}{# Heroes or Villains #}
{% endif %}{# Culture #}
{% if History %}
## History

### Timeline

Date | Name | Event
:---:|:----:|:----
{% for event in History.Timeline %}
{{ event.Date }} | {{ event.Name }} | {{ event.Description }}
{% endfor %}
{% endif %}{# History #}

{% endblock %}
