'''

Advent of Code - 2023 Day 9

'''


def readFile(filePath): # Reads the input puzzle file and returns 2D array of the number on each line
    lines = []
    with open(filePath, 'r') as file:
        for line in file:
            stringList = line.strip().split(" ") # Breaking line into words
            lines.append([int(item) for item in stringList]) # Converting each word to number and appending
    return lines


def forwardHistory(inputArray):

    # Base case
    is_all_zero = all(element == 0 for element in inputArray)
    if is_all_zero:
        return 0

    # Recursive Case
    else:
        diffs = []
        for i in range(0, len(inputArray) - 1):
            diffs.append(inputArray[i+1] - inputArray[i])
        return inputArray[-1] + forwardHistory(diffs)


def backwardHistory(inputArray):

    # Base case
    is_all_zero = all(element == 0 for element in inputArray)
    if is_all_zero:
        return 0

    # Recursive Case
    else:
        diffs = []
        for i in range(0, len(inputArray) - 1):
            diffs.append(inputArray[i+1] - inputArray[i])
        return inputArray[0] - backwardHistory(diffs)


if __name__ == "__main__":
    example = [10, 13, 16, 21, 30, 45]
    print(backwardHistory(example))

    allLines = readFile('puzzleInput.txt')
    forwardTotal = 0
    backwardTotal = 0
    for line in allLines:
        forwardTotal += forwardHistory(line)
        backwardTotal += backwardHistory(line)
        
    print(f'Forward Total: {forwardTotal}')
    print(f'Backward Total: {backwardTotal}')


    
