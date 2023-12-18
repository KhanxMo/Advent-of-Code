'''

Advent of Code - 2023 Day 1

'''

def readFile(filePath): # Reads the input puzzle file and returns 2D array of the number on each line
    linesOut = []

    with open(filePath, 'r') as file:
        for line in file:
            numList = []
            for char in line:
                if char.isdigit():
                    numList.append(char)
            linesOut.append(numList)

    return linesOut


def calVal(vals):
    if len(vals) == 1:
        return vals[0] + vals[0]
    elif len(vals) == 0:
        return ''
    else:
        return vals[0] + vals[-1]

if __name__ == "__main__":

    totalSum = 0
    allLines = readFile('puzzleInput.txt')

    for line in allLines:
        lineSum = int(calVal(line))
        totalSum += lineSum

    print(totalSum)


    print("one2three4")

