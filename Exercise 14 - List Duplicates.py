print "Please enter a list"
values = input()

def remove(values):
    newValues = []
    for value in values:
        if value not in newValues:
            newValues.append(value)
    return newValues

print remove(values)
raw_input()
