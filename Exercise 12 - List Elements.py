while (True):
    print "Please enter a list"
    userList = input()
    newList = [userList[0], userList[len(userList) - 1]]
    print newList
    print "Play again? 'yes'/'no'"
    playAgain = raw_input()
    if(playAgain == 'no'):
        break
    elif(playAgain == 'yes'):
        print ""
    else:
        print "You did not enter a valid response"
