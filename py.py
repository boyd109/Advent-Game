import random
import time
import sys

def isInteger(number):
    try:
        int(number)
        return True
    except ValueError:
         return False
        
def validskillpoint(number):
	if number > skillp or number < 0:
		number = raw_input("Please enter a valid number!")
		intLoop(number)
	else:
		return number

def intLoop (number):
    while not isInteger(number):
        number = raw_input("Enter the number")
    else:
        validskillpoint(int(number))

		
name = raw_input("What is your name")

micro = 20
skillp = 10
RNG = random.randint(0,100)
print "Hello %s" % name
time.sleep(1)
print "Your lottery ticket number for this session is: %i" % RNG
time.sleep(1)
print "Spend your %i points in Strength, Intelligence, and Luck" % skillp
time.sleep(1)
# Strength Points
print "Points remaining: %i" % skillp
time.sleep(1)
number = raw_input("Invest how many into Strength?")
intLoop(number)
number = int(number)
s = number
skillp = skillp - number

# Intelligence Points
print "Points remaining: %i" % skillp
time.sleep(1)
number = int(raw_input("Invest how many into Intelligence?"))
intLoop(number)
number = int(number)
i = number
skillp = skillp - number

# Luck Points
print "Points remaining: %i" % skillp
time.sleep(1)
number = int(raw_input("Invest how many into Luck?"))
intLoop(number)
number = int(number)
l = number
skillp = skillp - number

print "You stats are Strength: %i, Intelligence: %i, Luck:, %i" % (s,i,l)
time.sleep(1)
print "Start"

# Start of the Game
print "Please enter all choice with a single number. For example : 2"
print "You have been adventuring for days on end, with no food or water."
print "Up ahead you see what looks to be a pool of water."

#First Choice
c1 = int(raw_input("(1) Grab some water in your water bottle (2) Drink straight from the river"))

#time.sleep(1)
chance = random.randint(0, 2)
if chance + c1 > l:
    print "The inside of your throat starts to itch and you feel a burning sensation."
    print "The water must have been contaminated, and now you died."
    time.sleep(1)
    print "The End"
    sys.exit()
else:
    print "You continue on with some water."

#time.sleep(1)

print "You adventure until you reach a small town late in the night."
print "It has been a tiring day and you are not sure what tomorrow holds."

#Second Choice
c2 = int(raw_input("(1) look for a place to rest (2) Explore the town"))
chance = random.randint(0, 2)

if c2 == 1:
    print "You find a local hotel that gives you a room."
    print "After settling down, you lie on the bed and sleep."
    print "In the night you hear steps in the hallway"
    print "Suddenly, you are grabbed and you black out before noticing anything"
    time.sleep(1)
    print "The End"
    sys.exit()
    
if c2 == 2:
    if chance + c2 > s:
        print "Some armed thugs surround you."
        print "Some carry knives, others carry crude pipes and baseball bats."
        print "Outnumbered, you succumb to defeat."
        time.sleep(1)
        print "The End"
        sys.exit()
        
print "The brightly lit streets illuminate your path."
print "One vendor asks if you would like to buy something at their shop"
print "After politely saying no, you notice a small handgun pointed underneath you."
    
#Third Choice
c3 = int(raw_input("(1) Try to run (2) Try to talk calmly to the vendor"))
if c3 == 1:
    print "You start to run, and hear POP POP POP"
    print "You fall to the ground"
    time.sleep(1)
    print "The End"
    sys.exit()

if c3 == 2:
    print "You survived."
    print "The End"
    time.sleep(1)
    sys.exit()