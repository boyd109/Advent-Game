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
		return True

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

print "Spend your %i points in Strength, Intelligence, and Luck" % skillp

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
i = number
skillp = skillp - number

time.sleep(1)
print "You stats are Strength: %i, Intelligence: %i, Luck:, %l" % (s,i,l)
time.sleep(1)
print "Start"
