from enum import Enum
def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [line.split(" ") for line in inputLines]
        return inputLines

def partOne():
    input = parseInput()
    print(input)
def partTwo():
    input = parseInput()
    print(input)
    
partOne()
partTwo()