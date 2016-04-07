print "Please enter a number"
number = int(raw_input())
index = 0
fiboOne = 1
fiboTwo = 1
fiboThree = 2
lastPrinted = False
while(index < number):
    if(lastPrinted == False):
        print fiboOne
        lastPrinted = 'fiboOne'
        fiboOne = fiboTwo + fiboThree
    elif(lastPrinted == 'fiboOne'):
        print fiboTwo
        lastPrinted = 'fiboTwo'
        fiboTwo = fiboThree + fiboOne
    elif(lastPrinted == 'fiboTwo'):
        print fiboThree
        lastPrinted = 'fiboThree'
        fiboThree = fiboOne + fiboTwo
    elif(lastPrinted == 'fiboThree'):
        print fiboOne
        lastPrinted = 'fiboOne'
        fiboOne = fiboTwo + fiboThree
    else:
        print "An error occurred"
        break
    index = index + 1
raw_input()
