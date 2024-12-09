import re

expressionsToFind = "do\(\)|don\'t\(\)|mul\(\d+,\d+\)"
multiplierEnable = True
numbersToFind = "\d+"
multiTotal = 0

with open('day03-Input', 'r') as inputFile:
    string = inputFile.read()

find = re.findall(expressionsToFind, string)
for element in find:
    if element == "don't()":
        multiplierEnable = False
    else:
        if element == "do()":
            multiplierEnable = True
        else:
            if multiplierEnable:
                numbers = re.findall(numbersToFind, element)
                multiTotal = multiTotal + (int(numbers[0]) * int(numbers[1]))

print(multiTotal)
