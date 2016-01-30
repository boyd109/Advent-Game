import random
import time

name = raw_input("What is your name")
micro = 20
skillp = 8
RNG = random.randint(0,100)
print "Hello %s" % name
time.sleep(1)
print "Your lottery ticket number for this session is: %i" % RNG

print "Spend your %i points in Strength, Intelligence, and Luck" % skillp


print "Points remaining: %i" % skillp
try:
   s = int(raw_input("Invest how many into Strength?"))
except ValueError:
   print("That's not a whole number!")
while s > skillp or s < 0:
	print "Error Try Again"
	s = int(raw_input("Invest how many into Strength?"))
skillp = skillp - s

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
