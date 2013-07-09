#encoding: utf-8
import yaml
import codecs
from datetime import datetime, timedelta

IN = '2013-03-05-photos.md'
OUT = IN + '.new'

yaml_context = []
end = []

lang2folders = {
    'de':'de/fotos/',
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
        "fr":u"récréation"
    },
    "spycam":{
        "de":u"fotofalle",
        "en":u"spycam",
        "fr":u"spycam"
    } 
}
def _write_it(pic,date,tags,cats):

    for lang, folder in lang2folders.iteritems():
        for cat in cats:
            nd = {
                'lang':lang,
                'layout':'photo',
                'picname':pic,
                'categories':folder.split(',')+[cat],
                'tags':tags[:]
            }
            with codecs.open(folder+'/'+"%s-%s.md" % (date.strftime("%Y-%m-%d"),pic), 'w', encoding="utf-8") as outfh:
                outfh.write("---\n")
                outfh.write(yaml.safe_dump(nd))
                outfh.write("---\n")

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


def writeIt(o=o):
    date = datetime.strptime("2010-07-07","%Y-%m-%d")
    for pid in sorted(o["pics"].keys()):
        data =  o["pics"][pid]
        hiddentags = set(data["hiddentags"])
        _write_it(pid, date, data["tags"])
        date += timedelta(days=1)

def cleanIt():
    import os
    for lang, folder in lang2folders.iteritems():
        os.system("rm -rf %s" % folder)



def _get_categories(*tags):
    cats = []
    if some(lambda x: x in ('dead animal'  'hunter'  'hunting'), tags):
        cats.append("hunting")
    if some(lambda x: x in ('Album Action', 'offroad action', 'dune riding', 'dune'), tags):
        cats.append("action")
    if not some(lambda x: x in ( 'dead animal', 'painting' ), tags) and "animal" in tags:
        cats.append("animals")
    if not some(lambda x: x in ( 'dead animal', 'painting' ), tags) and "animal" in tags:
        cats.append("landscape")
def some(pred, coll):
    """ Returns the first element x in coll where pred(x) is logical true.
        If no such element is found, returns None.

        >>> fish_are_blue = lambda x: "blue" in x.lower() and "fish" in x.lower()
        >>> some(fish_are_blue,
        ...      ["Red fish", "Green fish", "Blue fish", "Blue and yellow fish"])
        'Blue fish'
        >>> some(fish_are_blue,
        ...      ["Red dog", "Green dog", "Blue dog", "Blue and yellow fish"])
        'Blue and yellow fish'
        >>> some(fish_are_blue,
        ...      ["Red dog", "Green dog", "Blue dog"])
    """
    for elem in coll:
        if pred(elem):
            return elem
    return None

    # for tag in data["tags"]:
    #     if "bei" in tag:
    #         stags.remove(tag)
    #         hiddentags.add(tag)
    #         stags.add(tag.replace("bei ",""))

    # o["pics"][pid]["tags"] = sorted(list(s.title() for s in stags))
    # o["pics"][pid]["hiddentags"] = sorted(list(hiddentags))

def saveIt(o=o):
    with codecs.open(OUT, 'w', encoding="utf-8") as outfh:
        outfh.write("---\n")
        outfh.write(yaml.safe_dump(o))
        outfh.write("---\n")
        # outfh.write("".join(end))

def addCategory(cat, titles, o=o):
    for key in o['pics'].keys():
        if o['pics'][key]['title'] in titles:
            if 'categories' not in o['pics'][key]:
                o['pics'][key]['categories']=[]
            if cat not in o['pics'][key]['categories']:
                o['pics'][key]['categories'].append(cat)

# o = yaml.load(open("in.yml"))

# # tags = set()
# bad = ["cave", "bright", "Shangri-La", "green water", "sneaking", "offroad cars", "sandy road", "hunting", "sky", "lake", "few clouds", "schlucht", "offroad car", "evening", "half moon", "giant rock", "photo camera", "hands", "drinking", "playing music", "blue sky", "clouds", "postcard", "hunt", "cloudy", "rocks", "sand", "plain", "river", "view", "tents", "pirsch", "jump", "sunrise", "great view", "archeology", "revier", "fountain", "cloudless", "nice view", "Gewehr", "blurry", "living room", "eating", "far away", "rock", "dune", "guitar", "path", "no clouds", "water", "sniper rifle", "drum", "hubschrauber", "waterfall", "wasserfall", "jumping", "road", "swimming", "replace", "canyon", "caves", "table", "essen", "singing", "sun set", "night", "pots", "sun rise", "rock climbing", "basin", "valley", "nice clouds", "mountains", "cross hair", "sand tracks", "silencer", "carrying", "rifle", "hole", "hunting spot", "car", "no cloud", "wind mill", "shower", "del", "broken car", "nice shot", "kissing", "sun down", "toilet", "golden mountain", "marmor", "rock painting", "mountain", "full moon", "offroad action", "puppy", "bird nest", "map", "del time", "splash water", "sun downer", "rain", "hand", "binoculars", "running", "plane", "arch", "desert", "heavy road", "beds", "sunset", "sun", "eating lunch", "painting", "playing", "child", "guy", "human", "hunter", "huntress", "kid", "man", "people", "person", "persons", "smoker", "woman", "women", "worker", "humans",]

# sbad = set(bad)

# for pid, data in o["pics"].iteritems():
# 	stags = set(data["tags"])
# 	newtags = stags - sbad
# 	hiddentags = stags & sbad
# 	if len(newtags) != len(stags):
# 		print pid, newtags, hiddentags
# 	o["pics"][pid]["tags"] = list(newtags)
# 	o["pics"][pid]["hiddentags"] = list(hiddentags)


# with codecs.open("in2.yml","w", encoding="utf-8") as fh:
# 	fh.write(yaml.safe_dump(o))
# with codecs.open("taglist.txt","w", encoding="utf-8") as fh:
# 	fh.write(u"\n".join(sorted(map(unicode, tags), key=unicode.lower)))

import re

titles = re.compile(r'"title": "([^"]+)"')

for x in ("action", "animals", "hunting", "landscape", "plants", "recreation", "spycam"):
    with open("done/%s.jl"%x) as fh:
        txt = fh.read()
        tits = titles.findall(txt)
        addCategory(x,tits)

saveIt()
