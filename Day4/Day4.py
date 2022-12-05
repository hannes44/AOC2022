from functools import reduce
def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip().replace('-',',').split(",") for line in input]
        return inputLines

def partOne():
    input = parseInput()
    # check if interval overlaps
    sum = reduce(lambda x, y: x + 1 if (int(y[0]) <= int(y[2]) and int(y[1]) >= int(y[3])) or (int(y[2]) <= int(y[0]) and int(y[3]) >= int(y[1])) else x, input, 0)
    print(sum)
def partTwo():
    input = parseInput()
    sectionIDs = list(map(lambda x: [list(range(int(x[0]), int(x[1])+1)), list(range(int(x[2]), int(x[3])+1))], input))
    # check if set of sectionIDs isn't of length 0
    sum = reduce(lambda x, y: x + 1 if len(set(y[0]) & set(y[1])) > 0 else x, sectionIDs, 0)
    print(sum)
partOne()
partTwo()