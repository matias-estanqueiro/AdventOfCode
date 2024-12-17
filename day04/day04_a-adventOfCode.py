import re

patternToFind = "XMAS|SAMX"
totalXmas = 0
i = 0
inputArray = []
rowXmas = ''
columnXmas = ''
diagonalXmasLeft = ''
diagonalXmasRight = ''

with open('day04-Input', 'r') as inputFile:
    # Coincidencias en cada fila
    for row in inputFile:
        row = row.strip()
        inputArray.append(list(row))
        rowXmas = rowXmas + ' ' + row
    
    matches = []
    for i in range(len(rowXmas)):
        match = re.match(patternToFind, rowXmas[i:])
        if match:
            matches.append(match.group())
    totalXmas = totalXmas + len(matches)

    # Coincidencias en cada columna
    for row in range(len(inputArray[0])):
        new_row = []
        for column in range(len(inputArray)):
            # Matriz transpuesta
            new_row.append(inputArray[column][row])
        columnXmas = columnXmas + ' ' + ''.join(new_row)
    
    matches = []
    for i in range(len(columnXmas)):
        match = re.match(patternToFind, columnXmas[i:])
        if match:
            matches.append(match.group())
    totalXmas = totalXmas + len(matches)
    
    rowQuantity = len(inputArray)
    columnQuantity = len(inputArray[0])

    # Coincidencias en la diagonal (arriba-abajo/izquierda-derecha)
    for diagonal in range(rowQuantity + columnQuantity - 1):
        rowResult = []
        for row in range(rowQuantity):
            column = diagonal - row
            if column >= 0 and column < columnQuantity:
                rowResult.append(inputArray[row][column])
        if diagonal % 2 == 0:
            diagonalXmasLeft = diagonalXmasLeft + ' ' + ''.join(rowResult[::-1])
        else:
            diagonalXmasLeft = diagonalXmasLeft + ' ' + ''.join(rowResult)

    matches = []
    for i in range(len(diagonalXmasLeft)):
        match = re.match(patternToFind, diagonalXmasLeft[i:])
        if match:
            matches.append(match.group())
    totalXmas = totalXmas + len(matches)
    
    # Coincidencias en la diagonal (arriba-abajo/derecha-izquierda)
    for diagonal in range(rowQuantity + columnQuantity - 2, -1, -1):
        rowResult = []
        for row in range(rowQuantity -1, -1, -1):
            column = diagonal - (rowQuantity - 1 - row)
            if column >= 0 and column < columnQuantity:
                rowResult.append(inputArray[row][column])
        diagonalXmasRight = diagonalXmasRight + ' ' + ''.join(rowResult[::-1])

    matches = []
    for i in range(len(diagonalXmasRight)):
        match = re.match(patternToFind, diagonalXmasRight[i:])
        if match:
            matches.append(match.group())
    totalXmas = totalXmas + len(matches)

print(totalXmas)


    

