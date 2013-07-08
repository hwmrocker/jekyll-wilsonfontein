---
layout: default
---
{% assign o = site.tags.hideme[0] %}

{%assign pic = o.pics[page.picname]%}


({{pic}})

<img src="/img/photos/{{ pic.url }}" />
©{{ pic.author}}

{% for tag in pic.tags %}
{{tag}} 
{% if forloop.rindex0 != 0 %}, {% endif %}
{% endfor %}

{{ content }}

<div id="page-navigation"> 
        <div class="clear">&nbsp;</div> 
        <div class="left"> 
        {% if page.previous.url %} 
                <a href="{{page.previous.url}}" title="Previous Post: 
{{page.previous.title}}">&laquo; {{page.previous.title}}</a> 
        {% endif %} 
        </div> 

        <div class="right"> 
        {% if page.next.url %} 
                <a href="{{page.next.url}}" title="next Post: 
{{page.next.title}}">{{page.next.title}} &raquo; </a> 
        {% endif %} 
        </div> 
        <div class="clear">&nbsp;</div> 
</div>