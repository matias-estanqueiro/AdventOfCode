# https://adventofcode.com/2024/day/2

from re import split

rowLevels = []
safeLevels = 0

def convertToInt(string):
    return int(string)

def isSafe(uncheckedLevel):
    increasing = True
    decreasing = True
    adyacent = True

    for element in range(len(uncheckedLevel) - 1):
        result = uncheckedLevel[element] - uncheckedLevel[element + 1]
        if result >= 0:
            increasing = False
            break

    for element in range(len(uncheckedLevel) - 1):
        result = uncheckedLevel[element] - uncheckedLevel[element + 1]
        if result <= 0:
            decreasing = False
            break

    for element in range(len(uncheckedLevel) - 1):
        result = abs(uncheckedLevel[element] - uncheckedLevel[element + 1])
        if not (1 <= result <= 3):
            adyacent = False
            break

    if (increasing or decreasing) and adyacent:
        return True
    else:
        return False


with open ('day02-Input', 'r') as inputFile:
    for row in inputFile:
        row = row.strip()
        rowLevels.append(split('\D+', row))
    
for level in rowLevels:
    increasing = True
    decreasing = True
    adyacent = True

    level = list(map(convertToInt, level))
    safeOrUnsafe = isSafe(level)

    if safeOrUnsafe:
        safeLevels = safeLevels + 1
    else:
        for element in range(len(level)):
            newLevel = level.copy()
            del newLevel[element]
            newOportunitySafe = isSafe(newLevel)
            if newOportunitySafe:
                safeLevels = safeLevels + 1
                break
            newLevel = []

print(safeLevels)
inputFile.close()