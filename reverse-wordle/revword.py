# reverse wordle
# given a sequence of random letters one at a time, try to form a valid word by committing to an ordering.

import string
import random
import os

# sets up a good wordlist and returns it
# the wordlist contains the complete list of acceptable words, i.e. "right answers" to the game
def wordlistsetup():
	letterSet = set(string.ascii_lowercase)
	list = []
	f = open("words.txt")
	for i in f.readlines():
		i = i.strip()
		i = i.lower()
		
		# checks for non-alpha characters
		if set(i).issubset(letterSet):
			list.append(i)
	return list

# generates the next letter
# "actual" is distributed according to english-language letter frequencies, and is recommended
# "equal" gives each letter a 1/26 chance of coming up, but likely leads to more unsolvable cases
def letterGenerator(version = "actual"):
	if version == "equal":
		return string.ascii_lowercase[random.randint(0,25)]
	
	# a list of weights for the random.choices(). corresponds to ["a".."z"]. prob of "e" is slightly raised to cover rounding error from wikipedia's letter frequency table
	weights = [.078, .02, .04, .038, .1141, .014, .03, .023, .086, .0021, .0097, .053, .027, .072, .061, .028, .0019, .073, .087, .067, .033, .01, .0091, .0027, .016, .0044]
	
	return random.choices(population = string.ascii_lowercase, weights = weights)[0]

def play(length, wordlist):
	answerString = ["_" for x in range(length)]
	for i in answerString: print(i, end = " ")
	print("")
	for n in range(length):
		print(n, end = " ")
	print("")
	
	# do the game
	while "_" in answerString:
	
		# pass in the argument "equal" if you want an equal 1/26 chance of getting each letter instead
		nextLetter = letterGenerator()
		
		index = input("your next letter is %s. indicate the index where you want it. > " %nextLetter)
		
		# checks for non-digit inputs, out-of-bounds inputs, and already-filled slots
		while not str.isdigit(index) or int(index) >= len(answerString) or answerString[int(index)] != "_":
			index = input("sorry! that index is invalid. try again, or face the consequences... > ")
		
		index = int(index)
		
		answerString = answerString[:index] + [nextLetter] + answerString[(index+1):]
		
		for i in answerString: print(i, end = " ")
		print("")
		for n in range(length):
			print(n, end = " ")
		print("")
	
	answerString = "".join(answerString)
	
	if answerString in wordlist:
		print("HOORAY! YOU DID IT! I'M SO PROUD OF YOU!!!")
	else:
		print("that isn't a word. i'm so sorry. try again")

def main():
	print("LOADING . . .")
	
	# set up the wordlist (the list of acceptable words)
	wordlist = wordlistsetup()
	
	# function to clear the screen before each new game
	clear = lambda: os.system('cls')
	
	# this is the default number of letters in the word. can range from 2-however high
	numLetters = 5
	
	# game loop
	while True:
		playAgain = input("play a game? 'y' or enter = yes, 'n' = no, # = number of letters in the word (default is 5, must be int of >=2) > ")
		if playAgain == "y" or playAgain == "": # initiate a new game
			clear()
			play(numLetters, wordlist)
		elif str.isdigit(playAgain) and int(playAgain) > 1:
			clear()
			numLetters = int(playAgain)
			play(numLetters, wordlist)
		else:
			break

if __name__ == "__main__":
	main()
