def parseInitialCrates():
    with open("initialCrates.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [line for line in inputLines]
        newInput = [[] for _ in range(9)]
        for y in inputLines:
            count = 0
            for x in range(1, len(y), 4):
                if y[x] != " ":
                    newInput[count].append(y[x])
                count += 1
        return newInput
    
def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip().split(" ") for line in input]
        inputLines = [[line[1], line[3], line[5]] for line in inputLines]
        return inputLines


def partOne():
    initialCrates = parseInitialCrates()
    input = parseInput()
    
    for x in input:
        for _ in range(int(x[0])):
            initialCrates[int(x[2])-1].insert(0, initialCrates[int(x[1])-1].pop(0))
    print(list(map(lambda x: x.pop(0),initialCrates)))

def partTwo():
    initialCrates = parseInitialCrates()
    input = parseInput()
    
    for x in input:
        subCrates = initialCrates[int(x[1])-1][:int(x[0])]
        for y in range(int(x[0])):
            initialCrates[int(x[1])-1].pop(0)
            initialCrates[int(x[2])-1].insert(0, subCrates.pop())
    print(list(map(lambda x: x.pop(0),initialCrates)))
    
partOne()
partTwo()