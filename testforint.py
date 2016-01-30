skillp = 8

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

number = raw_input("Please enter") 
while not isInteger(number):
    number = raw_input("Enter the number")
else:
    validskillpoint(int(number))