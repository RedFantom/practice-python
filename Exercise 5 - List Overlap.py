print "Please enter two lists"
listOne = input()
listTwo = input()
index = 0
newList = list()
for elementOne in listOne:
    for elementTwo in listTwo:
        if elementOne == elementTwo:
            newList.append(elementOne)
print "The overlap between the lists is:"
print newList
