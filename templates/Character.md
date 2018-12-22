{% extends 'base.md' %}

{% block title%}
{{ title }}
{% endblock %}

{% block summary %}
Character description for {{ title }}
{% endblock %}

{% block pagecontent %}
## General Info

- Race : {{ GeneralInfo.Race }}
- Age : {{ GeneralInfo.Age }}
- Traits :
{% for trait in GeneralInfo.Traits %}
    - {{ trait }}
{% endfor %}
{% if Occupation %}
## Occupation

- Role : {{ Occupation.Role }}
{% if Occupation.Note %}
    {{ Occupation.Note }}
{% endif %}{# Note #}
{% if Occupation.Location %}
- Location : {{ Occupation.Location }}
{% endif %}{# Location #}

{% endif %}{# Occupation #}
{% if Description %}
## Description

{{ Description }}
{% endif %}{# Description #}
{% endblock pagecontent %}

