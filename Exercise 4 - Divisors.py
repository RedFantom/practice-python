print "Please enter a number"
number = int(raw_input())
print "All the dividers of this number are:"
i = number
while i > 0:
    if(number % i == 0):
        print i
    i = i - 1
