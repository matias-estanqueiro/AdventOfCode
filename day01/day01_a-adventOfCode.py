# https://adventofcode.com/2024/day/1

totalDistance = 0
numberList1 = []
numberList2 = []

with open('day01-Input', 'r') as inputFile:
    # Considering the format of the file used as input for this exercise, we process it line by line, performing the following actions:
    #   1. We generate an array with the substrings found in the line.
    #   2. We convert the strings to int format, storing each of the positions of the array ([0] and [1]) into a new array of numeric elements.
    for row in inputFile:
        parsedRow = row.split()
        numberList1.append(int(parsedRow[0]))
        numberList2.append(int(parsedRow[1]))

# We sort the lists using a native Python function.
sortedArray = sorted(numberList1)
sortedArray2 = sorted(numberList2)

# We iterate through the first sorted array, performing the following actions:
#   1. We subtract the element in the same position of the second array and get the absolute value of that subtraction (difference).
#   2. We add the obtained value to the variable `totalDistance`.
for i in range(len(sortedArray)):
    totalDistance = totalDistance + abs(sortedArray[i] - sortedArray2[i])

print(totalDistance)
inputFile.close()
