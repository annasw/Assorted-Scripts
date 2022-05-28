"""
okay so here's what we're doing.
i'm curious to see how long it would take me to program an autocorrect
that is objectively better and more robust than the microsoft word version

my plan currently:
- take a word
- check if it is in the dictionary (simple hashtable lookup, O(1))
	- if so, we're done
	- if not...
- determine closest fits for simple operations (letter swaps, missing letter, extra letter, wrong letter)
	- multiple changes-- bruteforce?? better solution (please)??
- guess the intended word based on which requires the fewest changes
- if there's a tie, pick the one that is the most commonly used

- future functionality:
	- look at two-word clusters (three-word? ???) and see if there is a one-letter change that
	makes the resultant change MUCH MORE PROBABLE
	but i'm guessing frequency tables for two-word clusters are much harder to find...
	maybe just examine some huge repository of modern english? the internet??? maybe this exists.
	- recurse n layers deep for your choice of n
	(but honestly past 2 you're going to get some real gibberish getting guessed)
	- make it follow me around through all my windows and apps, making changes live
	- dynamically edit-able library
"""

from string import ascii_lowercase
from time import time # timing (optional)
# it's about 0.001s for a single one-off word,
# 0.06 for a single 2-off word,
# 0.001s for a sentence with all words off by one,
# a little over 0.2 for a sentence with all words off by two

#make dictionary
#keys: words, values: frequency (just an integer)
dict = {}
def populateDict():
	f = open("english.txt") # from https://github.com/nachocab/words-by-frequency
	for line in f.readlines():
		contents = line.split()
		dict[contents[1]] = int(contents[0])
	f.close()

# cheks for a better speling
# will do:
# - swaps of any two adjacent letters
# - adding a missing letter anywhere in the wrod
# - subtracting a letter anywhere in the wrod
# - swapping out any one letter for a replacement
# currently functional for one or two iterations
# starts with one, does two if it hasnt found a viable candidate
def spelChek(wrod, iteration = 0):
	# check for dumb shit
	for letter in wrod:
		if letter not in ascii_lowercase:
			return wrod
	
	candidates = []
	
	#swap adjacent
	for i in range(len(wrod)-1):
		tempWrod = wrod[:i] + wrod[i+1] + wrod[i] + wrod[i+2:]
		if tempWrod in dict:
			candidates.append(tempWrod)
		# these conditionals apply on the second (nth?) loop
		if iteration == 1:
			lastDitch = spelChek(tempWrod, 2)
			if lastDitch in dict:
				candidates.append(lastDitch)
	
	#addition
	for i in range(len(wrod)+1):
		for letter in ascii_lowercase:
			tempWrod = wrod[:i] + letter + wrod[i:]
			if tempWrod in dict:
				candidates.append(tempWrod)
			if iteration == 1:
				lastDitch = spelChek(tempWrod, 2)
				if lastDitch in dict:
					candidates.append(lastDitch)
	
	#removal
	for i in range(len(wrod)):
		tempWrod = wrod[:i] + wrod[i+1:]
		if tempWrod in dict:
			candidates.append(tempWrod)
		if iteration == 1:
			lastDitch = spelChek(tempWrod, 2)
			if lastDitch in dict:
				candidates.append(lastDitch)
	
	#replacement
	for i in range(len(wrod)):
		for letter in ascii_lowercase:
			tempWrod = wrod[:i] + letter + wrod[i+1:]
			if tempWrod in dict:
				candidates.append(tempWrod)
			if iteration == 1:
				lastDitch = spelChek(tempWrod, 2)
				if lastDitch in dict:
					candidates.append(lastDitch)
	
	# iterate once (technically recurse) if we havent found a good candidate
	if not candidates:
		if iteration == 0:
			return spelChek(wrod, 1)
		return wrod
	
	#print(candidates) # uncomment this if you want to see the set of candidate words
	
	# return the best (most popular) viable candidate
	bestCandidate = None
	popularity = 0
	for c in candidates:
		if dict[c] > popularity:
			bestCandidate = c
			popularity = dict[c]
	return bestCandidate


# like sisyphus, this method will forever request new wrods
# prints the fix if one exists
def main():
	populateDict()

	print("dis progam fixx wrods (snetences an nubmers OAKY!)")#, leters olny plz NOO NUBMER!!!")
	
	while True:
		snetence = input("gib wrod(s): ")
		
		wrods = snetence.split()
		words = []
		start = time()
		for wrod in wrods:
			wrod = wrod.lower()
			if wrod in dict or not wrod:
				words.append(wrod)
			else:
				words.append(spelChek(wrod))
		end = time()
		
		print("your wlecum: ", end = "")
		for word in words:
			print(word, end = " ")
		#print("\ndone in", end-start) # uncomment for timing
		print("\n")
	
if __name__ == "__main__":
	main()
