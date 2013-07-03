---
layout: default
---
{% assign o = site.tags.hideme[0] %}

{%assign pic = o.pics[page.picname]%}

({{pic}})

{{ pic.url}}

©{{ pic.author}}

{{ content }}