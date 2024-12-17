# https://adventofcode.com/2024/day/2

rowLevels = []
safeLevels = 0

def convertToInt(string):
    return int(string)
#########################

with open ('day02-Input', 'r') as inputFile:
    for row in inputFile:
    # The file is processed line by line, performing the following actions:
    #   1. We remove leading and trailing whitespaces from the line.
    #   2. We create an array with the substrings (in this case, numbers) found in the line.
        row = row.strip()
        rowLevels.append(row.split())

# rowLevels is an array of arrays.
for level in rowLevels:
    increasing = True
    decreasing = True
    adyacent = True

    # We convert the strings to integers to be able to perform operations.
    level = list(map(convertToInt, level))

    # For each element in the array level, we check if the difference between the current element and the next one is greater than or equal to 0.
    # If this condition is met, it means that the level is increasing. If the condition is not met, the level is considered no longer increasing 
    # and, therefore, is not a safe level.
    for element in range(len(level) - 1):
        result = level[element] - level[element + 1]
        if result >= 0:
            increasing = False
            break
    
    # For each element in the array level, we check if the difference between the current element and the next one is less than or equal to 0.
    # If this condition is met, it means that the level is decreasing. If the condition is not met, the level is considered no longer decreasing 
    # and, therefore, is not a safe level.
    for element in range(len(level) - 1):
        result = level[element] - level[element + 1]
        if result <= 0:
            decreasing = False
            break

    # Finally, we check if the element in the array has a difference between 1 and 3 with its next element.
    # If this condition is met, it means the level is safe. If the condition is not met, the level is considered unsafe.
    for element in range(len(level) - 1):
        result = abs(level[element] - level[element + 1])
        if not (1 <= result <= 3):
            adyacent = False
            break

    # To avoid unnecessary iterations through the array, once it is determined that the level is unsafe, the iteration is stopped using the 'break' statement.


    # If the level is safe, the variable 'safeLevels' is incremented.
    if (increasing or decreasing) and adyacent:
        safeLevels = safeLevels + 1

print(safeLevels)
inputFile.close()
