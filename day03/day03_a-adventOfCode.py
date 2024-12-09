import re

patternToFind = "mul\(\d+,\d+\)"
numbersToFind = "\d+"
multiTotal = 0

with open('day03-Input', 'r') as inputFile:
    string = inputFile.read()

find = re.findall(patternToFind, string)

for element in find:
    numbers = re.findall(numbersToFind, element)
    multiTotal = multiTotal + (int(numbers[0]) * int(numbers[1]))

print(multiTotal)