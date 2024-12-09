totalDistance = 0
numberList1 = []
numberList2 = []

with open('day01-Input', 'r') as inputFile:
    for row in inputFile:
        parsedRow = "".join(row.split())
        numberList1.append(int(parsedRow[0:5]))
        numberList2.append(int(parsedRow[5:10]))

sortedArray = sorted(numberList1)
sortedArray2 = sorted(numberList2)

for i in range(len(sortedArray)):
    totalDistance = totalDistance + abs(sortedArray[i] - sortedArray2[i])

print(totalDistance)
inputFile.close()