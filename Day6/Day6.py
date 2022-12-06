from functools import reduce
def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        return input[0]

def partOne():
    input = parseInput()
    count = 0
    for i, c in enumerate(input):
        if i < 4:
            count += 1
            continue
        subset = input[i-4:i]
        if reduce(lambda x, y: x if subset.count(y) == 1 else False, subset, True):
            print(count)
            return
        count +=1

def partTwo():
    input = parseInput()
    count = 0
    for i, c in enumerate(input):
        if i < 14:
            count += 1
            continue
        subset = input[i-14:i]
        if reduce(lambda x, y: x if subset.count(y) == 1 else False, subset, True):
            print(count)
            return
        count +=1
partOne()
partTwo()