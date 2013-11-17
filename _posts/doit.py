#encoding: utf-8
import yaml
import codecs
from datetime import datetime, timedelta
import os

# Helper functions
def some(pred, coll):
    for elem in coll:
        if pred(elem):
            return elem
    return None


IN = '2013-03-05-photos.md'
OUT = IN + '.new'
def load():
    yaml_context = []
    end = []
    yaml_context_idx = 0
    for line in codecs.open(IN, encoding="utf-8"):
        if line == "---\n":
            yaml_context_idx += 1
            # outfh.write(line)
            continue
        if yaml_context_idx == 1:
            yaml_context.append(line)
        elif yaml_context_idx > 1:
            end.append(line)

    o = yaml.load("\n".join(yaml_context))
    return o
o=None

#############################################################
# Translations

lang2folders = {
    'de':'de/fotos',
    'en':'en/photos',
    'fr':'fr/photos'
}
catlang = {
    "action":{
        "de":u"action",
        "en":u"action",
        "fr":u"action"
    },
    "animals":{
        "de":u"tiere",
        "en":u"animals",
        "fr":u"animaux"
    },
    "hunting":{
        "de":u"jagd",
        "en":u"hunting",
        "fr":u"chasse"
    },
    "landscape":{
        "de":u"landschaft",
        "en":u"landscape",
        "fr":u"paysage"
    },
    "plants":{
        "de":u"pflanzen",
        "en":u"plants",
        "fr":u"plantes"
    },
    "recreation":{
        "de":u"erholung",
        "en":u"recreation",
        "fr":u"recreation",
        # "fr":u"récréation"
    },
    "spycam":{
        "de":u"fotofalle",
        "en":u"spycam",
        "fr":u"spycam"
    },
    "none":{
        "de":"",
        "en":"",
        "fr":""
    }
}
#############################################################
# Album index pages

index_templ = """---
categories: [%(lang)s, %(photo_trans)s %(cat_comma)s]
lang: %(lang)s
layout: default
navname: photos
h1: %(photo_trans)s
p1: %(cat)s
---

{%% for post in site.posts %%}
    {%% assign category_size = post.categories | size %%}
    {%% assign pid = post.picname %%}
    {%% assign album_path = '%(album_path)s' %%}
    {%% if post.categories contains '%(lang)s' and post.categories contains '%(photo_trans)s' %(extra_cat)s and category_size == %(cat_size)d %%}{%% include photo_thumb.html param=pid param2=album_path %%}{%% endif %%}
{%% endfor %%}"""

extra_cat_templ = "and post.categories contains '%(cat)s'"
def createAlbumIndexHTMLPage(lang, cat):
    extra_cat = ""
    if cat is not None:
        extra_cat = extra_cat_templ % {"cat":cat}
    path = "%s/" % lang2folders[lang]
    if cat is not None:
        path += cat + "/"
    formatd ={
        "lang": lang,
        "cat_comma": ", %s" % cat if cat is not None else "",
        "cat": cat if cat is not None else "",
        "photo_trans": lang2folders[lang].split('/')[1],
        "extra_cat": extra_cat,
        "cat_size": 2 if cat is None else 3,
        "album_path": path
    }
    final_txt = index_templ % formatd

    if cat is None:
        path += "all/"
    os.system("mkdir -p %s" %path)
    path += "index.html"
    with open("../"+path, "w") as fh:
        fh.write(final_txt)

def createAllAlbumIndesHTMLPages():
    for lang in lang2folders.keys():
        for cat in catlang.keys():
            createAlbumIndexHTMLPage(lang, catlang[cat][lang])
        createAlbumIndexHTMLPage(lang, None)


# def update(o=o):
#     date = datetime.strptime("2010-07-07","%Y-%m-%d")
#     for pid in sorted(o["pics"].keys()):
#         o["pics"][pid]["pid"]=pid
#         o["pics"][pid]["date"]=date.strftime("%Y-%m-%d")
#         date += timedelta(days=1)


# def _write_it(pic,date,tags,cats):
#     for lang, folder in lang2folders.iteritems():
#         for cat in cats + ['none']:
#             nd = {
#                 'lang':lang,
#                 'layout':'photo',
#                 'picname':pic,
#                 'categories':folder.split(',')+[catlang[cat][lang]],
#                 'tags':tags[:]
#             }

#             _folder = "%s/%s" %(folder, "%s/"%cat if cat != "none" else "")
#             os.system("mkdir -p %s" %_folder)
#             with codecs.open(_folder+'/'+"%s-%s%s.md" % (date.strftime("%Y-%m-%d"),("%s-"%cat) if cat != "none" else "",pic), 'w', encoding="utf-8") as outfh:
#                 outfh.write("---\n")
#                 outfh.write(yaml.safe_dump(nd))
#                 outfh.write("---\n")

# def writeIt(o=o):
#     date = datetime.strptime("2010-07-07","%Y-%m-%d")
#     for pid in sorted(o["pics"].keys()):
#         data =  o["pics"][pid]
#         hiddentags = set(data["hiddentags"])
#         _write_it(pid, date, data["tags"], data.get("categories",[]))
#         date += timedelta(days=1)




def genfn(pic, cat=None):
    return "%s-%s%s" % (pic["date"],("%s-"%cat) if cat is not None else "",pic["pid"])
def genlnk(pic, cat=None, folder=None):
    if cat in (None, "none"):
        return "/%s/%s.html"%(folder,pic["pid"])
    return "/%s/%s/%s%s.html"%(folder,cat,("%s-"%cat) if cat is not None else "",pic["pid"])


def writeIt2(o=o):
    for cat in catlang.keys():
        if cat == "none": cat = None
        catlist=[p for p in o["pics"].itervalues() if (cat in p.get("categories",[]) or cat is None)]
        for idx, pic in enumerate(catlist):
            prev = catlist[idx-1] if idx > 0 else None
            next = catlist[idx+1] if (idx+1) < len(catlist) else None
            _write_it2(pic, cat, next, prev)

def _write_it2(pic, cat=None, next=None, prev=None):
    for lang, folder in lang2folders.iteritems():
        cats = folder.split('/')
        if cat is not None:
            cats += [catlang[cat][lang]]
        nd = {
            'lang':lang,
            'layout':'photo',
            'picname':pic["pid"],
            'categories':cats,
            'tags':pic["tags"][:],
            'next_photo':genlnk(next,cat,folder) if next is not None else None,
            'prev_photo':genlnk(prev,cat,folder) if prev is not None else None
        }

        _folder = "%s/%s" %(folder, "%s/"%cat if cat is not None else "")
        os.system("mkdir -p %s" %_folder)
        with codecs.open(_folder+'/%s.md'%genfn(pic, cat), 'w', encoding="utf-8") as outfh:
            outfh.write("---\n")
            outfh.write(yaml.safe_dump(nd))
            outfh.write("---\n")


def cleanIt():
    "delete all photos posts"
    import os
    for lang, folder in lang2folders.iteritems():
        os.system("rm -rf %s" % folder)



def _get_categories(*tags):
    "return categories from tags"
    cats = []
    if some(lambda x: x in ('dead animal'  'hunter'  'hunting'), tags):
        cats.append("hunting")
    if some(lambda x: x in ('Album Action', 'offroad action', 'dune riding', 'dune'), tags):
        cats.append("action")
    if not some(lambda x: x in ( 'dead animal', 'painting' ), tags) and "animal" in tags:
        cats.append("animals")
    if not some(lambda x: x in ( 'dead animal', 'painting' ), tags) and "animal" in tags:
        cats.append("landscape")


def saveImagesInfos(o=o):
    with codecs.open(OUT, 'w', encoding="utf-8") as outfh:
        outfh.write("---\n")
        outfh.write(yaml.safe_dump(o))
        outfh.write("---\n")
        # outfh.write("".join(end))

def addCategory(cat, titles, o=o):
    "???"
    for key in o['pics'].keys():
        if o['pics'][key]['title'] in titles:
            if 'categories' not in o['pics'][key]:
                o['pics'][key]['categories']=[]
            if cat not in o['pics'][key]['categories']:
                o['pics'][key]['categories'].append(cat)

def foo():
    import re

    titles = re.compile(r'"title": "([^"]+)"')

    for x in ("action", "animals", "hunting", "landscape", "plants", "recreation", "spycam"):
        with open("done/%s.jl"%x) as fh:
            txt = fh.read()
            tits = titles.findall(txt)
            addCategory(x,tits)

    saveImagesInfos()
