import random
import time

def isInteger(number):
    try:
        int(number)
        return True
    except ValueError:
         return False
        
def validskillpoint(number):
	if (number > skillp or number < 0):
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
skillp = 8
RNG = random.randint(0,100)
print "Hello %s" % name
time.sleep(1)
print "Your lottery ticket number for this session is: %i" % RNG
time.sleep(1)
print "Spend your %i points in Strength, Intelligence, and Luck" % skillp
time.sleep(1)
# Strength Points
print "Points remaining: %i" % skillp
number = raw_input("Invest how many into Strength?")
intLoop(number)
number = int(number)
s = number
skillp = skillp - number

# Intelligence Points
print "Points remaining: %i" % skillp
number = int(raw_input("Invest how many into Intelligence?"))
intLoop(number)
number = int(number)
i = number
skillp = skillp - number

# Luck Points
print "Points remaining: %i" % skillp
number = int(raw_input("Invest how many into Luck?"))
intLoop(number)
number = int(number)
l = number
skillp = skillp - number

print "You stats are Strength: %i, Intelligence: %i, Luck:, %i" % (s,i,l)
time.sleep(1)
print "Start"

print "Please enter all choice with a single number. For example : 2"
print "You have been adventuring for days on end, with no food or water."
print "Up ahead you see what looks to be a pool of water"
print "Do you: (1) Grab some water in your water bottle? (2) Drink straight from the river ?
