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