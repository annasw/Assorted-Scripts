# consecutive vowels
# based on xkcd #853
# https://xkcd.com/853/
# what, indeed, is the english word with the most consecutive vowels?
#
#
# ANSWER: a tie between AAAAAA and euouae. both very real and legitimate words.
# tied for 3rd are aeaea, aeaean, aieee, cadiueio, chaouia, cooeeing, guauaenok,
# miaoued, miaouing, pauiie, and of course munroe's answer of "queueing"
#
# i guess i get why he chose that one, even if euouae would have elicited a higher level of sexual arousal
#
#
# just for fun im going to do the same thing with CONSONANTS! leggo
#
# okay so
# if we let y count, the record is a staggering 13 consecutive consonants in "llanfairpwllgwyngyll"
# but some of those y's are definitely vowels (possibly also some w's)
# if we count y as a vowel, our new record is 7 consecutive consonants
# the list still does actually include "llanfairpwllgwyngyll," astonishingly
# it also includes pgnttrp (a VERY real word), substrstrata, and tsktsks (probably the legit recordholder)
#
# if we go down to 6 there are a LOT
# a few cool examples: archchronicler, bergschrund, catchphrase, a BUNCH of german, and the very obvious typo "offpspring"

import string

words = []
with open("english-words-master\words.txt") as f:
	words = [x.strip() for x in f.readlines()]

# every vowel
# whether y is a vowel or not is a matter of some debate and no little ambiguity
# adjust if u like, and adjust the floors accordingly
# i'm leaving it out by default because leaving it in affects the vowel answer
# which is like the primary goal of this script
vowelString = "aeiouAEIOU" # "aeiouAEIOUyY"

# it's almost too easy
consString = "".join([i for i in string.ascii_letters if i not in vowelString])

# takes a word
# returns the number of consecutive vowels in that word
def consecVowels(word):
	finalCount = 0
	runningCount = 0
	for i in word:
		if i in vowelString:
			runningCount += 1
			finalCount = max(finalCount, runningCount)
		else:
			runningCount = 0
	
	return finalCount

def solveForVowels():
	## do the actual thing i guess
	vowelDict = {} # keys = # of consec vowels, values = list of words with that #
	# let's set the floor at 5 consecutive vowels
	floor = 5
	# well done
	for word in words:
		vowels = consecVowels(word)
		if vowels >= floor:
			if vowelDict.get(vowels) == None:
				vowelDict[vowels] = [word]
			else:
				ls = vowelDict[vowels]
				ls.append(word)
				vowelDict[vowels] = ls

	for n in vowelDict:
		print(vowelDict[n])

# num of consec consonants
def consecCons(word):
	finalCount = 0
	runningCount = 0
	for i in word:
		if i in consString:
			runningCount += 1
			finalCount = max(finalCount, runningCount)
		else:
			runningCount = 0
	
	return finalCount

def solveForConsonants():
	consDict = {}
	floor = 6 # whatever you want; this one prints "archchronicler" though
	for word in words:
		consonants = consecCons(word)
		if consonants >= floor:
			if consDict.get(consonants) == None:
				consDict[consonants] = [word]
			else:
				ls = consDict[consonants]
				ls.append(word)
				consDict[consonants] = ls
	
	for n in consDict:
		print(consDict[n])

# pick one or both i guess
solveForVowels()
solveForConsonants()