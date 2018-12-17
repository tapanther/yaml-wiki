---
title: Republic of Siddarmark
summary: Main topic page for {{ title }}
authors: Juan P. Sierra
date: {{ date }}
---

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

# {{ title | title }}

## General Info

- Population : {{ GeneralInfo.Population | numberFormat }}
- Government : {{ GeneralInfo.Government }}
- Ethics :
{% for ethic in GeneralInfo.Ethics %}
    - {{ ethic }}
{% endfor %}

## Society

### Government

{{ Society.Government }}

### Prominent Figures and Organizations

{{ dictSection(Society.Organizations) }}

## Culture

{{ Culture.Description }}

### Core Beliefs

{% for belief in Culture.CoreBeliefs %}
- **{{ belief }}**
{% endfor %}

### Values

{% for value in Culture.Values %}
- {{ value }}
{% endfor %}

### Prejudices

{% for prej in Culture.Prejudices %}
- {{ prej }}
{% endfor %}

### Religion

{{ Culture.Religion }}

### Traditions

{{ dictList(Culture.Traditions) }}

### Heroes & Villains

#### Heroes

{{ dictList(Culture.Heroes) }}

#### Villains

{{ dictList(Culture.Villains) }}

## History

### Timeline

Date | Name | Event
:---:|:----:|:----
{% for event in History.PivotalEvents %}
{{ event.Date }} | {{ event.Name }} | {{ event.Description }}
{% endfor %}