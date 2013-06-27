import yaml
import codecs

o = yaml.load(open("in.yml"))

# tags = set()
bad = ["cave", "bright", "Shangri-La", "green water", "sneaking", "offroad cars", "sandy road", "hunting", "sky", "lake", "few clouds", "schlucht", "offroad car", "evening", "half moon", "giant rock", "photo camera", "hands", "drinking", "playing music", "blue sky", "clouds", "postcard", "hunt", "cloudy", "rocks", "sand", "plain", "river", "view", "tents", "pirsch", "jump", "sunrise", "great view", "archeology", "revier", "fountain", "cloudless", "nice view", "Gewehr", "blurry", "living room", "eating", "far away", "rock", "dune", "guitar", "path", "no clouds", "water", "sniper rifle", "drum", "hubschrauber", "waterfall", "wasserfall", "jumping", "road", "swimming", "replace", "canyon", "caves", "table", "essen", "singing", "sun set", "night", "pots", "sun rise", "rock climbing", "basin", "valley", "nice clouds", "mountains", "cross hair", "sand tracks", "silencer", "carrying", "rifle", "hole", "hunting spot", "car", "no cloud", "wind mill", "shower", "del", "broken car", "nice shot", "kissing", "sun down", "toilet", "golden mountain", "marmor", "rock painting", "mountain", "full moon", "offroad action", "puppy", "bird nest", "map", "del time", "splash water", "sun downer", "rain", "hand", "binoculars", "running", "plane", "arch", "desert", "heavy road", "beds", "sunset", "sun", "eating lunch", "painting", "playing", "child", "guy", "human", "hunter", "huntress", "kid", "man", "people", "person", "persons", "smoker", "woman", "women", "worker", "humans",]

sbad = set(bad)

for pid, data in o["pics"].iteritems():
	stags = set(data["tags"])
	newtags = stags - sbad
	hiddentags = stags & sbad
	if len(newtags) != len(stags):
		print pid, newtags, hiddentags
	o["pics"][pid]["tags"] = list(newtags)
	o["pics"][pid]["hiddentags"] = list(hiddentags)


with codecs.open("in2.yml","w", encoding="utf-8") as fh:
	fh.write(yaml.safe_dump(o))
# with codecs.open("taglist.txt","w", encoding="utf-8") as fh:
# 	fh.write(u"\n".join(sorted(map(unicode, tags), key=unicode.lower)))
