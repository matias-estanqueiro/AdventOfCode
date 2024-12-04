acumulator = 0
array2occurrencies = {}

numberList1 = []
numberList2 = []

with open('day01-Input', 'r') as inputFile:
    for row in inputFile:
        parsedRow = "".join(row.split())
        numberList1.append(int(parsedRow[0:5]))
        numberList2.append(int(parsedRow[5:10]))

for element in numberList2:
    if element in array2occurrencies:
        array2occurrencies[element] = array2occurrencies[element] + 1
    else:
        array2occurrencies[element] = 1

for element in numberList1:
    if element in array2occurrencies:
        acumulator = acumulator + (array2occurrencies[element] * element)

print(acumulator)