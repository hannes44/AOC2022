from functools import reduce
import math
def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [line for line in inputLines]
        newInput = []
        count = -1
        for i, x in enumerate(inputLines):
            #print(x)
            if "Monkey" in x:
                newInput.append([])
                count +=1
            if "Operation" in x:
                newInput[count].append(x.split("=")[1].strip().split(" "))
            if "Starting" in x:
                newInput[count].append(x.split(":")[1].strip().split(","))
            if "divisible" in x:
                newInput[count].append(x.split("by")[1].strip())
            if "true" in x:
                newInput[count].append(x.split("monkey")[1].strip())
            if "false" in x:
                newInput[count].append(x.split("monkey")[1].strip())
        for i,x in enumerate(newInput):
            newInput[i] = Monkey(x[0], x[1], x[2], x[3], x[4])
        return newInput
class Monkey:
    def __init__(self, starting, operation, divisible, onTrue, onFalse):
        self.currentItems = [int(x) for x in starting]
        self.divisible = int(divisible)
        self.operation = operation
        self.onTrue = int(onTrue)
        self.onFalse = int(onFalse)

def partOne():
    input = parseInput()
    inspectCount = [0 for x in range(len(input))]
    for x in range(0, 20):
        for k, monkey in enumerate(input):
            while(len(monkey.currentItems) != 0):
                inspectCount[k] += 1
                # worry level increased
                if "old" == monkey.operation[0] and "old" == monkey.operation[2]:
                    if "*" in monkey.operation:
                        input[k].currentItems[0] *= input[k].currentItems[0]
                    if "+" in monkey.operation:
                        input[k].currentItems[0] += input[k].currentItems[0]
                else:
                    if "*" in monkey.operation:
                        input[k].currentItems[0] *= int(monkey.operation[2])
                    if "+" in monkey.operation:
                        input[k].currentItems[0] += int(monkey.operation[2])
                     
                # worry level decreased
                input[k].currentItems[0] = input[k].currentItems[0] // 3
                
                if input[k].currentItems[0] % monkey.divisible == 0:
                    input[monkey.onTrue].currentItems.append(input[k].currentItems[0])
                    input[k].currentItems.pop(0)
                else:
                    input[monkey.onFalse].currentItems.append(input[k].currentItems[0]) 
                    input[k].currentItems.pop(0)
    inspectCount.sort()           
    print(inspectCount[-1] * inspectCount[-2])
                
def partTwo():
    input = parseInput()
    inspectCount = [0 for x in range(len(input))]
    commonMultiplier = reduce(lambda a,b: a*b, [x.divisible for x in input])
    for x in range(0, 10000):
        for k, monkey in enumerate(input):
            while(len(monkey.currentItems) != 0):
                inspectCount[k] += 1
                # worry level increased
                if "old" == monkey.operation[0] and "old" == monkey.operation[2]:
                    if "*" in monkey.operation:
                        input[k].currentItems[0] *= input[k].currentItems[0]
                    if "+" in monkey.operation:
                        input[k].currentItems[0] += input[k].currentItems[0]
                else:
                    if "*" in monkey.operation:
                        input[k].currentItems[0] *= int(monkey.operation[2])
                    if "+" in monkey.operation:
                        input[k].currentItems[0] += int(monkey.operation[2])
                     
                # worry level decreased
                input[k].currentItems[0] = (input[k].currentItems[0]) % commonMultiplier
                
                if input[k].currentItems[0] % monkey.divisible == 0:
                    input[monkey.onTrue].currentItems.append(input[k].currentItems[0])
                    input[k].currentItems.pop(0)
                else:
                    input[monkey.onFalse].currentItems.append(input[k].currentItems[0]) 
                    input[k].currentItems.pop(0)
    inspectCount.sort()           
    print(inspectCount[-1] * inspectCount[-2])
    
partOne()
partTwo()