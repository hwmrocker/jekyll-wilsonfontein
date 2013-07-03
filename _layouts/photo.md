---
layout: default
---
{% assign o = site.tags.hideme[0] %}

{%assign pic = o.pics[page.picname]%}
{%assign page.title = "foo"%}


({{pic}})

<img src="/img/photos/{{ pic.url }}" />
©{{ pic.author}}

{% for tag in pic.tags %}
{{tag}} 
{% if forloop.rindex0 != 0 %}, {% endif %}
{% endfor %}

{{ content }}