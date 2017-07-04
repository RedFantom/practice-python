print "Please enter a list in the form of [n, n, n]"
numbers = input()
new_numbers = list()
index = 0
print "Please enter the number you want to be the maximum"
condition = int(raw_input())
for number in numbers:
    if(number <= condition):
        print number
        new_numbers.append(number)
        index = index + 1
print new_numbers
