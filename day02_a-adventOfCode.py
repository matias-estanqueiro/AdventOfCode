from re import split
rowLevels = []
levelResults = []

safeLevels = 0

def convertToInt(string):
    return int(string)


with open ('day02-Input', 'r') as inputFile:
    for row in inputFile:
        row = row.strip()
        rowLevels.append(split('\D+', row))
    
for level in rowLevels:
    level = list(map(convertToInt, level))
    for element in range(len(level)-1):
        result = level[element] - level[element + 1]
        levelResults.append(result)
    
    if all(1 <= num <= 3 for num in levelResults):
        safeLevels = safeLevels + 1
    
    if all(-3 <= num <= -1 for num in levelResults):
        safeLevels = safeLevels + 1
    levelResults = []
    
print(safeLevels)
inputFile.close()