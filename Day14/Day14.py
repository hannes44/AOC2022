import re
def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip().replace(">", "").replace(" ", "") for line in input]
        inputLines = [re.split('-', line) for line in inputLines]
        inputLines = [[x.split(",") for x in line] for line in inputLines]
        for i,x in enumerate(inputLines):
            inputLines[i] = [[int(x[0]), int(x[1])] for x in inputLines[i]]
        
       # inputLines = [[int(x) for x in line] for line in inputLines]
        return inputLines

def calculateCordinateInterval(cordinates):
    lowestX = 100000
    highestX = 0
    highestY = 0
    for x in cordinates:
        for y in x:
            if y[0] > highestX:
                highestX = y[0]
            if y[0] < lowestX:
                lowestX = y[0]
            if y[1] > highestY:
                highestY = y[1]
    return [lowestX, highestX, highestY]

def addLinesToMap(map, cordinates, xOffset):
    for x in cordinates:
        prevCordinate = -1
        for y in x:
            if prevCordinate == -1:
                prevCordinate = [y[0] - xOffset, y[1]]
                continue
            if prevCordinate[0] < y[0] - xOffset:
                for i in range(prevCordinate[0], y[0] - xOffset + 1):
                    map[prevCordinate[1]][i] = "#"
            else:
                for i in range(y[0] - xOffset, prevCordinate[0] +1):
                    map[prevCordinate[1]][i] = "#"
            if prevCordinate[1] < y[1]:
                for i in range(prevCordinate[1], y[1] + 1):
                    map[i][y[0] - xOffset] = "#"
            else:
                for i in range(y[1], prevCordinate[1] + 1):
                    map[i][y[0] - xOffset] = "#"
            prevCordinate = [y[0] - xOffset, y[1]]

def isBlockUnderSand(map, sandCordinate):
    count = 1
    while(True):
        if sandCordinate[1] + count > len(map)-1:
            return False
        if map[sandCordinate[1]+count][sandCordinate[0]] == "#":
            return True
        count += 1

def partOne():
    input = parseInput()
    sandSpawnCoordinates = [500, 0]
    xOffset, highestXValue, highestYValue = calculateCordinateInterval(input)
    sandSpawnCoordinates = [sandSpawnCoordinates[0] - xOffset, sandSpawnCoordinates[1]]
    map = [["." for _ in range(highestXValue - xOffset + 1)] for _ in range(highestYValue+1)]
    
    addLinesToMap(map, input, xOffset)
    done = False
    sandCount = 0
    while(not done):
        currentCordinate = sandSpawnCoordinates.copy()
        while(currentCordinate[0] >= 0 and currentCordinate[0] < len(map[0]) and currentCordinate[1] >= 0 and currentCordinate[1] < len(map)):
            # move sand one step down
            if currentCordinate[1]+1 < highestYValue and map[currentCordinate[1]+1][currentCordinate[0]] == ".":
                currentCordinate[1] += 1
                continue
            else:
                if not currentCordinate[0]-1 < 0 and not currentCordinate[1] + 1 > len(map)-1  and map[currentCordinate[1]+1][currentCordinate[0]-1] == ".":
                    currentCordinate = [currentCordinate[0]-1, currentCordinate[1]+1]
                    continue
                if not currentCordinate[0]+1 > len(map[0]) - 1 and not currentCordinate[1] + 1 > len(map) -1 and map[currentCordinate[1]+1][currentCordinate[0]+1] == ".":
                    currentCordinate = [currentCordinate[0]+1, currentCordinate[1]+1]
                    continue
                else:
                    if currentCordinate[0]-1 < 0 and map[currentCordinate[1]+1][currentCordinate[0]+1] != ".":
                        done = True
                        break
                    if currentCordinate[0]+1 > len(map[0]) and map[currentCordinate[1]+1][currentCordinate[0]-1] != ".":
                        done = True
                        break
                    if not isBlockUnderSand(map, currentCordinate):
                        done = True
                        break
                    sandCount += 1
                    map[currentCordinate[1]][currentCordinate[0]] = "O"    
                    break
    print(sandCount)
            
def partTwo():
    input = parseInput()
    sandSpawnCoordinates = [500, 0]
    xOffset, highestXValue, highestYValue = calculateCordinateInterval(input)
    sandSpawnCoordinates = [sandSpawnCoordinates[0] - xOffset, sandSpawnCoordinates[1]]
    map = [["." for _ in range(highestXValue - xOffset+1)] for _ in range(highestYValue+1)]
    
    
    addLinesToMap(map, input, xOffset)

    for i, x in enumerate(map):
        for y in range(0,500):
            map[i].append(".")
            map[i] = ["."] + map[i]
    map.append(["." for _ in range(0, len(map[0]))])
    map.append(["#" for _ in range(0, len(map[0]))])

    sandSpawnCoordinates = [sandSpawnCoordinates[0] + 500, sandSpawnCoordinates[1]]
    done = False
    sandCount = 0
    while(not done):
        currentCordinate = sandSpawnCoordinates.copy()
        while(currentCordinate[0] >= 0 and currentCordinate[0] < len(map[0]) and currentCordinate[1] >= 0 and currentCordinate[1] < len(map)):
            # if start is stand, done
            if map[sandSpawnCoordinates[1]][sandSpawnCoordinates[0]] == "O":
                done = True
                break
            # move sand one step down if not blocked
            if currentCordinate[1]+1 < len(map)-1 and map[currentCordinate[1]+1][currentCordinate[0]] == ".":
                currentCordinate[1] += 1
                continue
            else:
                # try to move diagonally
                if not currentCordinate[0]-1 < 0 and not currentCordinate[1] + 1 > len(map) - 1  and map[currentCordinate[1]+1][currentCordinate[0]-1] == ".":
                    currentCordinate = [currentCordinate[0]-1, currentCordinate[1]+1]
                    continue
                if not currentCordinate[0]+1 > len(map[0]) - 1 and not currentCordinate[1] + 1 > len(map) -1 and map[currentCordinate[1]+1][currentCordinate[0]+1] == ".":
                    currentCordinate = [currentCordinate[0]+1, currentCordinate[1]+1]
                    continue
                else:
                    # if both diagonals are blocked add sand to map
                    sandCount += 1
                    map[currentCordinate[1]][currentCordinate[0]] = "O"    
                    break
    print(sandCount)
    
partOne()
partTwo()