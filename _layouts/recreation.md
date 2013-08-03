---
layout: default

navname: recreation

links:
    de:
        url: /de/erholung.html
        name: Erholung
    en:
        url: /en/recreation.html
        name: Recreation
    fr:
        url: /fr/detente.html
        name: Détente
trans:
    h1:
        de: Erholung
        en: Recreation
        fr: Détente
    title:
        de: Erholen auf der Jagd Farm Wilsonfontein
        en: Recreation is very important to us
        fr: Détente
    h_1:
        de: Erholung wird bei uns **groß** geschrieben
        en: Recreation is very important to us
        fr: Chez nous le repos s’écrit en lettres **capitales**

    p_1:
        de: Lassen Sie vom Alltagsstress ab und genießen Sie die einmalige Landschaft. Hier werden Sie keine störenden Anrufe bekommen, sondern können es sich bei einer Farmrundfahrt gemütlich machen. Nach der Jagd können Sie die Wanderung an dem Bay Weg machen oder sich in Ihrem luxuriösem Zimmer ausruhen.
        en: Release the stress and enjoy the unique landscape. Here you will not get annoying phone calls but can make yourself comfortable on a farm tour. After the hunt you can walk along the Bay Pad or relax in your luxurious room.
        fr: Oubliez le stress du quotidien et appréciez la beauté du paysage. Chez nous vous ne serez pas dérangés par des coups de fils incessants et pourrez apprécier en toute sérénité les promenades sur la propriété. Après la chasse vous pourrez faire une randonnée le long du sentier historique du „Bay trail“, ou tout simplement profiter du confort de votre chambre.

    p_2:
        de: Wir bieten Ihnen zwei sehr schöne Zweibett Zimmer mit einem eigenen Waffenschrank, einer eigenen Dusche und Toilette.
    p_3:
        de: Neben der Möglichkeit sich ins Zimmer zurückzuziehen, kann man auch auf der Terrasse lesen und den Sonnenuntergang bewundern. Es gibt auch einen schönen Grillplatz an dem man Abends zusammen sitzen, sich am Lagerfeuer unterhalten und die Sterne genießen kann.

    p_4:
        de: Auch für das leibliche Wohl ist gesorgt. Unsere Köchin Frederika zaubert jeden Tag etwas schmack- und nahrhaftes auf den Tisch. Sie versteht es sehr gut, das auf der Farm erlegte (Bio) Wild, abwechslungsreich und immer köstlich zuzubereiten.
---

{{ page.trans.h_1[page.lang]}}
------------------------------

{{ page.trans.p_1[page.lang] | markdownify }}

<!-- P[136,59] -->
{% include double_image.html param="P0000059" param2="P0000135" %}

{{ page.trans.p_2[page.lang] | markdownify }}

{% include double_image.html param="P0000297" param2="P0000298" %}
<!-- P[311,312] -->

{{ page.trans.p_3[page.lang] | markdownify }}

{% include double_image.html param="P0000235" param2="P0000299" %}
{% include double_image.html param="P0000294" param2="P0000293" %}
<!-- P[313,248] -->
<!-- P[87,307] -->
{{ page.trans.p_4[page.lang] | markdownify }}

{{ content }}