print "Please enter a string"
string = raw_input()
stringLength = len(string)
index = 0
palindrome = False
if(stringLength % 2 == 0):
    stringHalf = stringLength / 2
    while(index < stringHalf):
        if(string[index] != string[(stringLength - 1) - index]):
            print "The string you entered is not a Palindrome"
            palindrome = False
            break
        else:
            palindrome = True
            index = index + 1
    if(palindrome == True):
        print "Congratulations! The string you entered is a Palindrome!"
elif(stringLength % 2 == 1):
    stringHalf = (stringLength - 1) / 2
    while (index < stringHalf):
        if(string[index] != string[(stringLength - 1) - index]):
            print "The string you entered is not a Palindrome"
            palindrome = False
            break
        else:
            palindrome = True
            index = index + 1
    if(palindrome == True):
        print "Congratulations! The string you entered is a Palindrome!"
else:
    print "An error has occurred"
