from re import split

rowLevels = []
safeLevels = 0

def convertToInt(string):
    return int(string)

with open ('day02-Input', 'r') as inputFile:
    for row in inputFile:
        row = row.strip()
        rowLevels.append(split('\D+', row))
    
for level in rowLevels:
    increasing = True
    decreasing = True
    adyacent = True

    level = list(map(convertToInt, level))

    for element in range(len(level) - 1):
        result = level[element] - level[element + 1]
        if result >= 0:
            increasing = False
            break
    
    for element in range(len(level) - 1):
        result = level[element] - level[element + 1]
        if result <= 0:
            decreasing = False
            break

    for element in range(len(level) - 1):
        result = abs(level[element] - level[element + 1])
        if not (1 <= result <= 3):
            adyacent = False
            break

    if (increasing or decreasing) and adyacent:
        safeLevels = safeLevels + 1
    
print(safeLevels)
inputFile.close()
