skillp = 8

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

number = raw_input("Int?")

while not isInteger(number):
        number = raw_input("Enter the number")
else:
        validskillpoint(int(number))