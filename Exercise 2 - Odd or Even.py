print "Please enter a number:"
number = int(raw_input())
if(number % 2 == 0):
    if(number % 4 == 0):
        print "Your number was a multiple of four"
    else:
        print "Your number was even"
elif(number % 2 == 1):
    print "Your number was odd"
else:
    print "An error has occurred"
    