# okay
# uhh
# i think my goal here was to produce all possible team names for the rwby team from rwby
# the best is obviously rawboy
# other strong contenders: barrow-boy, owerby, and iwberry

import re


with open("english-words-master\words.txt") as f:
	text = f.read()

rwbyWords = re.findall("r[aeiou]*w[aeiou]*b[aeiou]*y",text)

print(rwbyWords)


rwbySet = set("rwby")
otherConsonants = set("cdfghjklmnpqstvxz")
rwbyList = []
t = text.split()
for word in t:
	if rwbySet.issubset(word) and otherConsonants.isdisjoint(word) and not word[0].isupper():
		rwbyList.append(word)

print(rwbyList)
