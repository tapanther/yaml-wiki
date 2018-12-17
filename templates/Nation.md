{% extends 'base.md' %}

{% block title%}
{{ title }}
{% endblock %}

{% block summary %}
Main Page for {{ title }}
{% endblock %}

{% block pagecontent %}
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

{{ macros.dictSection(Society.Organizations) }}

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

{{ macros.dictList(Culture.Traditions) }}

### Heroes & Villains

#### Heroes

{{ macros.dictList(Culture.Heroes) }}

#### Villains

{{ macros.dictList(Culture.Villains) }}

## History

### Timeline

Date | Name | Event
:---:|:----:|:----
{% for event in History.PivotalEvents %}
{{ event.Date }} | {{ event.Name }} | {{ event.Description }}
{% endfor %}

{% endblock %}