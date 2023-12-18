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


def historyCalc(inputArray):

    # Base case
    is_all_zero = all(element == 0 for element in inputArray)
    if is_all_zero:
        return 0

    # Recursive Case
    else:
        diffs = []
        for i in range(0, len(inputArray) - 1):
            diffs.append(inputArray[i+1] - inputArray[i])
        return inputArray[-1] + historyCalc(diffs)


if __name__ == "__main__":
    example = [1, 3, 6, 10, 15, 21]
    print(historyCalc(example))

    allLines = readFile('puzzleInput.txt')
    total = 0
    for line in allLines:
        total += historyCalc(line)
        
    print(total)

    
