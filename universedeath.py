# so the basic question is this:
# given a finite plane (or cube, or sphere, or w/e),
# and given two randomly-selected points on that plane,
# what is the average distance between them, relative to the dimensions of the plane?
# (i think there's probably a very easy answer for this in prob
# but i'm not a nerd you guys)
# 
# the goal here is to (very roughly) estimate the answer to the following question:
# suppose that the universe is a false vacuum
# suppose also that somewhere in the universe, a "truer vacuum" has formed.
# how long, on average, can we, on Earth, expect to survive before we are destroyed?
#
# fun stuff.
# 
# anyway, i think we can estimate this by figuring out the approximate ratio of avg distance:plane size
# and work with the very rough idea we have about the size of the universe
# (which really isn't like a very good estimate but it doesn't even matter anyway
# given that afaik we have no way of estimating WHEN a truer vacuum will form.
# or did form. could've been yesterday. two light-days away.)

import random
from math import sqrt

# for the purposes of this exercise we will assume the universe is a cube
# which it's probably not but will suffice for our purposes

# one must compute the distance between two points (call them triples) in 3-space (call it a shoebox)
# one feels compelled to do this intuitively, without the use of google
# after all
# there will be no google when this "universe" is destroyed by a better, stronger, truer vacuum
def distance(a, b):
	x1, y1, z1 = a[0], a[1], a[2]
	x2, y2, z2 = b[0], b[1], b[2] # this is excellent naming practice
	
	distA = sqrt((x2-x1)**2 + (y2-y1)**2)
	distB = sqrt(distA**2 + (z2-z1)**2) # so is this
	
	# which one of course strongly prefers to the amateurish
	# and frankly sad
	# return sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
	
	return distB

# and now of course the vegan meat-substitute of the thing
# this one's faulty
"""maxTrials = 100000 # 100k
universeSize = 93000000000 # 93 billion you nerds
						   # (i.e. the appx size of the universe in l.y.)
						   # oh btw universe axes are 0-93bil, no negatives

totDist = 0
totTrials = 0

for t in range(maxTrials):
	nums = [] # locations in 3space of the earth and our beloved mother oblivion
	for e in range(6):
		nums.append(random.randint(0, universeSize))
	totDist += distance((nums[0], nums[1], nums[2]),(nums[3], nums[4], nums[5]))
	# wait i should have just handed distance() six numbers
	# god dammit
	totTrials += 1

print("your average Distance to Death (actually time) is: ", totDist/totTrials, " years.")"""

# this one is superior
avgs = []
for size in [100,200,300,400,500,600,700,800,900,1000]:
	trials = 100000 # 100k
	totDist = 0
	totTrials = 0
	
	for t in range(trials):
		nums = [] # locations in 3space of the earth and our beloved mother oblivion
		for e in range(6):
			nums.append(random.randint(0, size))
		totDist += distance((nums[0], nums[1], nums[2]),(nums[3], nums[4], nums[5]))
		totTrials += 1
	
	avgs.append(totDist/totTrials)

for i in avgs: print(i)

# the answer is around 61 billion years.
# now a few notes.
# a) it's lower than that, for a few reasons.
#   #1: the universe is not a cube (or is it?). i'm assuming it's closer to a sphere, or maybe like
# 	    an ellipse or some shit. idk. regardless, there are going to be fewer extremes
#	    with one off in the corner. i assume that lowers the avg dist.
#  	    i guess we could repeat this experiment (lol) with a sphere, but fuck it.
#	    (update from the future: i looked it up and for a sphere, the answer is (36/35)R, so c.46 billion years)
#   #2: it's possible we know something about the location of the earth relative
#	    to the universe? no idea what, but i'd assume that bc the earth has been around
#	    for an appreciable fraction of the length of the universe's existence,
#	    probably we're going to be slightly closer on avg to the death bubble.
#	    i would expect.
#   #3: the universe is -- allegedly -- expanding, so the number's going to keep going up.
#       in other words, the longer it takes for the vacuum to pop up, the longer we'll have between that and death.
# b) again, this assumes that the new, truer vacuum comes into being right now
#	 at a random point. which who knows if either of those things are true.
#	 could be in existence right now. could be right behind you. (literally.)
#	 could wait for a hundred trillion years, in which case the math's gonna be
#	 a little different. or maybe we're bedrock. maybe we're the ones who get to live
#	 forever. totally plausible, you guys. i don't even know what the phrase
#	 "cognitive bias" MEANS, much less have one!
#	 now our only problem is climate change. ur welcome guys
#
# one last thing. what does this tell us about the answer to the original math problem?
# if i were a harder-working young lady i would run it again w/ a bunch of universe sizes and look for an answer.
# so i'm gonna do that.
# i aspire to be the version of me i make fun of in my comments.
# brb.
#
# okay so basically the avg dist is 2/3rds the side length of the cube
# which, okay. fine.
# i feel like that should make some kind of sense if i think about it
# but if i thought about things then why would i need computers lol
#
# okay i looked up the actual answer and it is around .66
# the math is awful
# but the answer is sound
# cs wins again... kinda