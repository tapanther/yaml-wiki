{% extends 'base.md' %}

{% block title %}
{{ title }}
{% endblock %}

{% block summary %}
Character description for {{ title }}
{% endblock %}

{% block pagecontent %}
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

{{ Description | auto_link }}
{% endif %}{# Description #}
{% if NotableEvents %}
## Notable Events

{% filter auto_link %}
{{ macros.dictList(NotableEvents) }}
{% endfilter %}

{% endif %}{# Notable Events #}
{% endblock pagecontent %}

