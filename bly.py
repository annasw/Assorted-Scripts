# okay so one of the few spelling mistakes i regularly make is mixing up words ending -ible/-ibly (e.g. irresistibly) and those ending -able/-ably (e.g. avoidably)
# and i can't find a reasonable rule for when one or the other applies
# so instead i did a superficial comparison of frequency of occurrence (in lexicon, to be clear, not usage) (ps i also frequently misspell "occurrence")
# because i just don't have any other solutions																(which relative frequency, -ance vs -ence, is virtually 1:1, btw)
# idk this is embarrassing
#
# so how common are the endings -ibly vs -ably? (n.b. i also expanded this to include -able/-ible because it seemed like a good idea)
# let's
# find
# out

f = open("english-words-master\words.txt") # found here https://github.com/dwyl/english-words i wont bring it here though youre responsibile for your own decisions
ablyCount = 0
iblyCount = 0
for i in f:
	words = [x.strip() for x in f.readlines()]
	for w in words:
		if w[-4:] == "ably" or w[-4:] == "able": ablyCount += 1; print(w) # i guess you can comment these out if you're a coward and dont want 7000 words printing on your screen or ide or output or whatever real programmers use
		if w[-4:] == "ibly" or w[-4:] == "ible": iblyCount += 1; print(w.upper()) #semicolonsinpython <- that one's a hashtag
f.close()

print("-ably count:", ablyCount, "\n" + "-ibly count:", iblyCount)

# this comment is down here because of spoilers
# the answer is that -ably occurs about 4x more frequently than -ibly, and when you include -able/-ible, the a's have it 11:2
# you're welcome

# i guess you could generalize this pretty easily if you were so inclined
# it is literally just a list of words
