import copy
def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [line.split(" ")[0] for line in inputLines]
        parsedInput = [[]]
        count = 0
        for x in input:
            if x == '\n':
                count +=1
                parsedInput.append([])
                continue
            parsedInput[count].append(eval(x.replace("\n", "")))
        return parsedInput

def evaluateExpression(firstExpression, secondExpression):
    if type(firstExpression) == int and type(secondExpression) == int:
        if firstExpression < secondExpression:
            return True
        elif firstExpression > secondExpression:
            return False
        if firstExpression == secondExpression:
            return None
    if type(firstExpression) == list and type(secondExpression) == int:
        secondExpression = [secondExpression]
    if type(firstExpression) == int and type(secondExpression) == list:
        firstExpression = [firstExpression]
    while(True):
        if len(firstExpression) > 0:
            exp = firstExpression.pop(0)
            if len(secondExpression) > 0:
                exp2 = secondExpression.pop(0)
                evaledExp = evaluateExpression(exp, exp2)
                if evaledExp == True:
                    return True
                if evaledExp == False:
                    return False
            else:
                return False
        else:
            if len(secondExpression) == 0 and len(firstExpression) == 0:
                return None
            if len(secondExpression) > 0:
                return True
            else:
                return False
    return False

def partOne():
    input = parseInput()
    correctIndexes = []
    for i, x in enumerate(input):
        firstExpression = x[0]
        secondExpression = x[1]
        if evaluateExpression(firstExpression, secondExpression) == True:
            correctIndexes.append(i+1)
    print(sum(correctIndexes))
    
    
def parseInputPartTwo():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [eval(line.split(" ")[0]) for line in inputLines if line != '']
        return inputLines

def partTwo():
    input = parseInputPartTwo()
    input.append([[2]])
    input.append([[6]])    
    
    # using bubble sort 
    for x in range(len(input)):
        swapped = False
        for i, y in enumerate(input):
            if i == len(input)-1:
                continue
            evalResult = evaluateExpression(copy.deepcopy(input[i]), copy.deepcopy(input[i+1]))
            if evalResult == False:
                #swap
                swapped = True
                input[i], input[i+1] = input[i+1], input[i]
        if swapped == False:
            break
    sum = 1
    for i, x in enumerate(input):
        if x == [[2]] or x == [[6]]:
            sum *=(i+1)
    print(sum)

partOne()
partTwo()