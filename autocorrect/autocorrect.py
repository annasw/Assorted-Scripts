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
	- THIS MIGHT BE TRICKY
	- multiple changes-- guess?? better solution (please)??
	- FOR NOW we'll just do one change.
- guess the intended word based on which requires the fewest changes
	- THIS IS ALSO GOING TO BE TRICKY
- if there's a tie, pick the one that is the most commonly used
	- this will require a very big table of word uses


- future functionality:
	- look at two-word clusters (three-word? ???) and see if there is a one-letter change that
	makes the resultant change MUCH MORE PROBABLE
	but i'm guessing frequency tables for two-word clusters are much harder to find...
	maybe just examine some huge repository of modern english? the internet??? maybe this exists.
"""

from string import ascii_lowercase

#make dictionary
#keys: words, values: frequency (just an integer)
dict = {}
def populateDict():
	f = open("english-words-master\english.txt") # from https://github.com/nachocab/words-by-frequency
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
# currently it only does one iteration because 2+ iteration make number go up big fast :(
def spelChek(wrod):
	# check for dumb shit
	wrod = wrod.lower()
	for letter in wrod:
		if letter not in ascii_lowercase:
			print("NOO!!!!! VEWY BADD!!!!! TWY AGIAN!!!")
			return None
	
	candidates = []
	
	#swap adjacent
	for i in range(len(wrod)-1):
		tempWrod = wrod[:i] + wrod[i+1] + wrod[i] + wrod[i+2:]
		if tempWrod in dict:
			candidates.append(tempWrod)
	
	#addition
	for i in range(len(wrod)+1):
		for letter in ascii_lowercase:
			tempWrod = wrod[:i] + letter + wrod[i:]
			if tempWrod in dict:
				candidates.append(tempWrod)
	
	#removal
	for i in range(len(wrod)):
		tempWrod = wrod[:i] + wrod[i+1:]
		if tempWrod in dict:
			candidates.append(tempWrod)
	
	#replacement
	for i in range(len(wrod)):
		for letter in ascii_lowercase:
			tempWrod = wrod[:i] + letter + wrod[i+1:]
			if tempWrod in dict:
				candidates.append(tempWrod)
	
	# pick the best candidato tomato
	if not candidates: return wrod
	
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

	print("dis progam fixx wrods, leters olny plz NOO NUBMER!!!")
	
	while True:
		wrod = input("gib wrod: ")
		
		if wrod in dict or not wrod:
			word = wrod
		else:
			word = spelChek(wrod)
		
		print("your wlecum:", word, "\n")
	
if __name__ == "__main__":
	main()
