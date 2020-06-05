{% extends 'base.md' %}

{% block title %}
{{ title }}
{% endblock %}

{% block summary %}
Description for {{ title }}
{% endblock %}

{% block pagecontent %}
{% if Mission %}
## Mission

- Role : {{ Mission.Role }}
{% if Mission.Note %}

    {{ Mission.Note }}
    
{% endif %}{# Note #}
{% if Mission.Location %}
- Location : {{ Mission.Location }}
{% endif %}{# Location #}

{% endif %}{# Mission #}
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

