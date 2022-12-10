def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [line.split(" ") for line in inputLines]
        return inputLines

def partOne():
    input = parseInput()
    xRegister = 1
    cyclesToCheck = [20, 60, 100, 140, 180, 220]
    cyclesCount = 0
    addOnNextCycle = False
    prevValue = -1
    signalStrengths = []
    haveAdded = False
    for i, x in enumerate(input):
        if cyclesCount in cyclesToCheck:
            signalStrengths.append(xRegister * cyclesCount) 
            haveAdded = True
        if addOnNextCycle:
            addOnNextCycle = False
            xRegister += int(prevValue)      

        # noop command
        if len(x) == 1:
            cyclesCount += 1
            continue
        
        for y in range(0, 2):
            if cyclesCount in cyclesToCheck and not haveAdded:
                signalStrengths.append(xRegister * cyclesCount) 
            haveAdded = False
            cyclesCount += 1
            addOnNextCycle = True
            prevValue = x[1]
    print(sum(signalStrengths))

def drawPixel(cyclesCount, xRegister):
    if (cyclesCount-1) % 40 == 0:
        print()
    if ((cyclesCount-1) % 40) in [xRegister-1, xRegister, xRegister+1]:
        print('#', end='')
    else:
        print('.', end='')

def partTwo():  
    input = parseInput()
    xRegister = 1
    cyclesToCheck = [20, 60, 100, 140, 180, 220]
    cyclesCount = 0
    addOnNextCycle = False
    prevValue = -1
    signalStrengths = []
    haveAdded = False
    for i, x in enumerate(input):
        if cyclesCount in cyclesToCheck:
            signalStrengths.append(xRegister * cyclesCount) 
            haveAdded = True
        if addOnNextCycle:
            addOnNextCycle = False
            xRegister += int(prevValue)      
        # noop command
        if len(x) == 1:
            cyclesCount += 1
            drawPixel(cyclesCount, xRegister)
            continue
        
        for y in range(0, 2):
            if cyclesCount in cyclesToCheck and not haveAdded:
                signalStrengths.append(xRegister * cyclesCount) 
            haveAdded = False
            cyclesCount += 1
            drawPixel(cyclesCount, xRegister)
            addOnNextCycle = True
            prevValue = x[1]
    
partOne()
partTwo()