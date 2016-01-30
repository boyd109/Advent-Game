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
	    while not isInteger(number):
	        number = raw_input("Enter the number")
	    else:
	        number = raw_input("Enter the number")
	        validskillpoint(int(number))
	else:
		return True
		
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
number = int(raw_input("Invest how many into Strength?"))
while not isInteger(number):
    number = raw_input("Enter the number")
else:
    validskillpoint(int(number))
skillp = skillp - number



# Intelligence Points


print "Points remaining: %i" % skillp
i = int(raw_input("Invest how many into Intelligence?"))
while i > skillp or i < 0:
	print "Error"
	i = int(raw_input("Invest how many into Intelligence?"))
skillp = skillp - i

print "Points remaining: %i" % skillp
l = int(raw_input("Invest how many into Luck?"))
while l > skillp or l < 0:
	print "Error"
	l = int(raw_input("Invest how many into Luck?"))
skillp = skillp - l

time.sleep(1)
print "You stats are Strength: %i, Intelligence: %i, Luck:, %l" % (s,i,l)
time.sleep(1)
print "Start"
