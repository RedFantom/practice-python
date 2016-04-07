def prime(number):
    index = 2
    primeProperty = True
    while(index < number):
        if(number % index == 0):
            primeProperty = False
            break
        index = index + 1
    return primeProperty

while(True):
    print "Please enter a number"
    userNumber = int(raw_input())
    userPrime = prime(userNumber)
    if(userPrime == True):
        print "Congratulations, your number is a prime!"
    elif(userPrime == False):
        print "Too bad, your number is not a prime..."
    else:
        print "An error has occurred"
        break
    print " "
    print "Do you want to play again? ('yes'/'no')"
    playAgain = raw_input()
    if(playAgain == 'no'):
        print "Thanks for playing!"
        break
    elif(playAgain == 'yes'):
        print ""
    else:
        print "You did not enter a valid response, the program will now quit"
        break
raw_input()
