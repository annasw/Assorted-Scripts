'''see README for more details'''

# binary search implementation
# 90% of programmers get it wrong (hashtag clickbait)
# can i get it right???
# probably not.

# takes an array and a desired value
# returns the index of the value in the array
# if index not in array, returns -1
def recursiveSearch(array, goal, bottom, top):
	# need to check for empty lists too
	
	if top==bottom:
		if array[top] == goal:
			return top
		else:
			return -1
	if abs(top-bottom)==1:
		if array[top]==goal: return top
		if array[bottom]==goal: return bottom
		else: return -1
	
	pivot = (top+bottom)/2
	if array[pivot] == goal:
		return pivot
	if array[pivot]>goal:
		top = pivot
	if array[pivot]<goal:
		bottom = pivot
	
	return recursiveSearch(array, goal, bottom, top)

def binarySearch(ls, g):
	if len(ls)==0: return -1
	else:
		return recursiveSearch(ls, g, 0, len(ls)-1)

import random # this is the first line I added during tests

def main():
	works = True
	for testCycle in range(50):
		ls = sorted([random.randint(1,50) for x in range(30)])
		goalNum = random.randint(1,50)
		i = binarySearch(ls, goalNum)

		# check that goalNum is in the right place
		if i!=-1 and ls[i]!=goalNum:
			works = False
			break

		# check that goalNum not in ls
		if i==-1 and goalNum in ls:
			works = False
			break
	
	print works

if __name__=="__main__":
	main()