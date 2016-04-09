print "Please enter a string"
string = raw_input()
stringList = string.split()
stringLength = len(stringList)
index = stringLength - 1
newString = ""
while(index > -1):
    newString = newString + stringList[index] + " "
    index = index - 1
print newString
raw_input()
