import random

timesPlayed = 0

while(True):
    random.seed()
    randomNumber = random.randint(1, 9)
    print "Your random number (1 through 9) has been determined"
    while(True):
        print "Please guess now: "
        guess = int(raw_input())
        if(guess == randomNumber):
            print "That's it!"
            break
        elif(guess < randomNumber):
            print "Your guess is too low"
        elif(guess > randomNumber):
            print "Your guess is too high"
        elif(guess > 9):
            print "You guessed above 9, please do not do so"
        elif(guess < 1):
            print "You guessed below 1, please do not do so"
        else:
            print "An error occurred, program will now quit"
            break
    print "Do you want to play again? ('yes'/'no')"
    timesPlayed = timesPlayed + 1
    playAgain = raw_input()
    if(playAgain == 'no'):
        print "You played ", timesPlayed, " times"
        break
    else:
        print ""
