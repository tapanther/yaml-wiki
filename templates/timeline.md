{% set title = 'Timeline' %}
{% extends 'base.md' %}

{% block title %}
Timeline
{% endblock %}

{% block summary %}
Combined Timeline from all pages
{% endblock %}

{% block addMeta %}
hide_toc: true
{% endblock %}

{% block pagecontent %}

| Year | Event | Description |
|:----:|:-----:|:------------|
{% for event in timeline %}
| {{ event.Date }} | {{ event.Name }} | {{ event.Description }} |
{% endfor %}

{% endblock pagecontent %}