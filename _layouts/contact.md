---
layout: default

navname: contact

links:
    de:
        url: /de/kontakt.html
        name: Kontakt
    en:
        url: /en/contact.html
        name: Contact
    fr:
        url: /fr/contact.html
        name: Contact
trans:
    h1:
        de: Kontakt
        en: Contact
        fr: Contact
    title:
        de: Kontakt
        en: Contact
        fr: Contact

    h_namibia:
        de: In Namibia
        en: In Namibia
        fr: En Namibie
    h_germany:
        de: In Deutschland
        en: In Germany
        fr: En Allemagne
    h_email:
        de: Per Email
        en: By Email
        fr: Par E-mail
    email:
        de: Schreiben sie mir eine Email an **namibhunt@hotmail.com**.
        en: Please write me an email at **namibhunt@hotmail.com**.
        fr: Please write me an email at **namibhunt@hotmail.com**.
    h_testimonials:
        de: Referenzen
        en: Testimonials
        fr: Testimonials
    testimonials:
        de: Folgende zufriedene Kunden haben sich bereit erklärt als Referenz zur Verfügung zu stehen.
        en: The following of our satisfied customers have agreed to be available as a reference.
        fr: La suite de nos clients satisfaits ont accepté d'agir à titre de référence.
    cell:
        en: Cell
        fr: Mobile
        de: Handy
    tel:
        en: Tel
        fr: Tél
        de: Tel
    fax:
        en: Fax
        fr: Fax
        de: Fax
---

###{{page.trans.h_namibia[page.lang]}}:
<!-- 
Ingo Gladis<br>
P.O. Box 40<br>
Karibib -->
<address class="vcard">
  <span class="fn">Ingo Gladis</span><br>
  <span class="adr">
    <span class="street-address">P.O. Box 40</span><br>
    <span class="locality">Karibib</span><br>
    <span class="country-name">Namibia</span>
  </span><br><br>
  <!-- <span class="tel-home-description">{{page.trans.tel[page.lang]}}:</span><span class="tel home">+264 (0) 64 - 55 08 90</span> <br>-->
  <span class="tel-home-description">{{page.trans.cell[page.lang]}}:</span><span class="tel cell">+264 (0) 81 - 3003 857</span><br>
</address>




###{{page.trans.h_germany[page.lang]}}:
<!-- 
Ingo Gladis<br>
Fasanstr. 18 <br>
84539 Ampfing -->
<address class="vcard">
  <span class="fn">Ingo Gladis</span><br>
  <span class="adr">
    <span class="street-address">Fasanstr. 18</span><br>
    <span class="postal-code">D-85439</span>
    <span class="locality">Ampfing</span><br>
    <span class="country-name">Deutschland</span>
  </span><br><br>
  <span class="tel-home-description">{{page.trans.tel[page.lang]}}:</span><span class="tel home">+49 (0) 8636 - 98 60 30</span><br>
  <span class="tel-fax-description">{{page.trans.fax[page.lang]}}:</span><span class="tel fax">+49 (0) 8636 - 98 60 31</span><br>
  <span class="tel-cell-description">{{page.trans.cell[page.lang]}}:</span><span class="tel cell">+49 (0) 176 - 38 80 30 80</span><br>
</address>


### {{page.trans.h_email[page.lang]}}
{{page.trans.email[page.lang] | markdownify}}
<!-- Please write me an email at **namibhunt@hotmail.com**. -->

### {{page.trans.h_testimonials[page.lang]}}
{{page.trans.testimonials[page.lang] | markdownify}}
<!-- The following of our satisfied customers have agreed to be available as a reference. -->

Hans Fuleda     **hans@fuleda.de**<br>
Axel Raabe       **a.raabe@gmx.net**<br>
Franz Baumann **baufra1@web.de**<br>
Philipp Jaeger **pj.envirofaune@wanadoo.fr**<br>
Max.H.Nübel   **nuebel@wohnstift-mozart.de**<br>
Dr. Udo Krappe  **udo.krappe@altana.com**<br>


{{ content }}