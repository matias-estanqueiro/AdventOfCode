inputArray = []
count = 0

with open('day04-Input', 'r') as inputFile:
    for row in inputFile:
        row = row.strip()
        inputArray.append(list(row))

for i, row in enumerate(inputArray):
    for j, element in enumerate(row):
        if element == 'A':
            # Verificar que los índices no están fuera de los límites
            if i > 0 and j > 0 and i < len(inputArray) - 1 and j < len(inputArray[0]) - 1:
                if inputArray[i-1][j-1] == 'M' and inputArray[i-1][j+1] == 'M' and inputArray[i+1][j-1] == 'S' and inputArray[i+1][j+1] == 'S':
                    count = count + 1
                if inputArray[i-1][j-1] == 'M' and inputArray[i-1][j+1] == 'S' and inputArray[i+1][j-1] == 'M' and inputArray[i+1][j+1] == 'S':
                    count = count + 1
                if inputArray[i-1][j-1] == 'S' and inputArray[i-1][j+1] == 'M' and inputArray[i+1][j-1] == 'S' and inputArray[i+1][j+1] == 'M':
                    count = count + 1
                if inputArray[i-1][j-1] == 'S' and inputArray[i-1][j+1] == 'S' and inputArray[i+1][j-1] == 'M' and inputArray[i+1][j+1] == 'M':
                    count = count + 1

print(count)