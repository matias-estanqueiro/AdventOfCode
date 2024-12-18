# https://adventofcode.com/2024/day/2

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
#########################

with open ('day02-Input', 'r') as inputFile:
    for row in inputFile:
        row = row.strip()
        rowLevels.append(row.split())
    
for level in rowLevels:
    level = list(map(convertToInt, level))
    safe = isSafe(level)

    if safe:
        safeLevels = safeLevels + 1
    else:
        # If the level is not safe, each of its elements is iterated over, removing one at a time and checking if the resulting level is safe.
        for element in range(len(level)):
            # A copy of the level is created
            newLevel = level.copy()
            # The element is removed
            del newLevel[element]
            newOportunitySafe = isSafe(newLevel)
            # If removing one of its elements makes the resulting level safe, the counter of safe levels is incremented, and the loop is exited.
            if newOportunitySafe:
                safeLevels = safeLevels + 1
                break
            newLevel = []

print(safeLevels)
inputFile.close()
