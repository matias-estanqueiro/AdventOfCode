# https://adventofcode.com/2024/day/1

acumulator = 0
array2occurrencies = {}

numberList1 = []
numberList2 = []

with open('day01-Input', 'r') as inputFile:
    for row in inputFile:
        parsedRow = row.split()
        numberList1.append(int(parsedRow[0]))
        numberList2.append(int(parsedRow[1]))

for number in numberList2:
    # A dictionary (array2occurrencies) is used, which, through its 'key : value' structure, allows us to store the occurrences of numbers, where 'key' 
    # is the number itself and 'value' is the count of repetitions of that number in the list 'numberList2'. In this way:
    #   1. If the number already exists in the dictionary, we increase its count of repetitions.
    #   2. If the number is not in the dictionary, we add it with a count of repetitions equal to 1.
    if number in array2occurrencies:
        array2occurrencies[number] = array2occurrencies[number] + 1
    else:
        array2occurrencies[number] = 1

# Finally, we iterate through 'numberList1' and check if each number is in the dictionary 'array2occurrencies'. If so, we multiply 
# the count of repetitions (value) by the number and add it to the variable 'acumulator'.
for number in numberList1:
    if number in array2occurrencies:
        acumulator = acumulator + (array2occurrencies[number] * number)

print(acumulator)
inputFile.close()
