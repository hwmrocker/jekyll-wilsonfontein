---
layout: default

navname: home

links:
    de:
        url: /de/index.html
        name: Home
    en:
        url: /en/index.html
        name: Home
    fr:
        url: /fr/index.html
        name: Home


picinfo:
    fr: Flowering Aloes front of the Hottentotten church.
    en: Flowering Aloes front of the Hottentotten church.
    de: Blühende Aloes vor der Hottentottenkirche.
---

{% assign description = page.picinfo[page.lang] %}
{% include image.html param='P0000197' param2=description %}

{{ content }}