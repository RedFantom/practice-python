import random

wins = 0
losses = 0
ties = 0
dictionary = { 1:'Rock', 2:'Paper', 3:'scissors'}
while(True):
    print "Please enter 'rock', 'paper' or 'scissors'"
    playerMove = raw_input()
    random.seed()
    compNumber = random.randint(1, 3)
    if(playerMove == 'rock'):
        playerNumber = 1
    elif(playerMove == 'paper'):
        playerNumber = 2
    elif(playerMove == 'scissors'):
        playerNumber = 3
    else:
        print "You did not enter a valid move. The program will now quit"
        break
    if(playerNumber == compNumber):
        print "The computer chose: ", dictionary[compNumber]
        print "Oh no, it's a tie!"
        ties = ties + 1
    elif(playerNumber == 1 and compNumber == 2):
        print "The computer chose: ", dictionary[compNumber]
        print "Oh no, you lost!"
        losses = losses + 1
    elif(playerNumber == 1 and compNumber == 3):
        print "The computer chose: ", dictionary[compNumber]
        print "Congratulations, you won!"
        wins = wins + 1
    elif(playerNumber == 2 and compNumber == 1):
        print "The computer chose: ", dictionary[compNumber]
        print "Congratulations, you won!"
        wins = wins + 1
    elif(playerNumber == 2 and compNumber == 3):
        print "The computer chose: ", dictionary[compNumber]
        print "Oh no, you lost!"
        losses = losses + 1
    elif(playerNumber == 3 and compNumber == 1):
        print "The computer chose: ", dictionary[compNumber]
        print "Oh no, you lost!"
        losses = losses + 1
    elif(playerNumber == 3 and compNumber == 2):
        print "The computer chose: ", dictionary[compNumber]
        print "Congratulations, you won!"
        wins = wins + 1
    print "Wins: ", wins, " Losses: ", losses, " Ties: ", ties
    print ""
    print "Do you want to play again? ('yes'/'no')"
    playAgain = raw_input()
    if(playAgain == 'no'):
        break
    elif(playAgain == 'yes'):
        print ""
    else:
        "You did not enter 'yes'/'no', the program will now exit"
        break
print "Thanks for playing! Your score was:"
print "Wins: ", wins, " Losses: ", losses, " Ties: ", ties
