# 1s
#
# given a number n, how many 1s are needed to write out all the numbers from 0 to n?
# then find the smallest n>1 such that f(n)=n
# from the google labs aptitude test
#
# this solution is O(n) altho i wonder whether there's some spooky closed-form formula
# we do it in O(n) and not some horrifying O(n^2) simply by tracking the last count at each step,
# and feeding that back into the method.
# it runs in 0.135 seconds.
# oh i guess technically it's O(n*k) where k is the number of digits in numbers that contain a 1
# which is basically O(n) unless we're dealing with numbers at such a scale that O(n) is basically O(infinity).
# 
# the answer is (spoilers) 199981.
# this problem constitutes the sequence A014778 in the OEIS https://oeis.org/A014778 of which our solution is a(3)
# it's finite and there are 84 total terms.
#
# i also wrote a loop to generate all the entries in A014778 for fun
# it's slow tho

import time

start = time.time()

def f(n, lastCount):
	chars = str(n)
	if "1" not in chars: return lastCount # we dont need to increment unless there's a 1 in the number
	for c in chars:
		if c == "1":
			lastCount += 1
	
	return lastCount

# this is the solution to the actual GLAT
n = 2 # we're starting at 2
count = 1
while n != count:
	n += 1
	count = f(n, count)

# this is just a fun little way to generate the whole list of A014778
# it takes a LOOOONG time to run (891.6 seconds, or just under 15 minutes)
# because the largest number in the set, 1111111110, is over 1 billion
# which is a lot for my computer to compute in an O(n) algorithm
'''
n = 0
count = 0
ls = []
while len(ls)<84: #heehee
	count = f(n, count)
	if n == count:
		ls.append(int(n))
	n += 1
'''
	
end = time.time()

print("n is", n, "count is", count)
#print("list:", ls)
print("ran in",end-start)