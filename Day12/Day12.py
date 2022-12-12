def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [line.split(" ")[0] for line in inputLines]
        return inputLines

def findPossibleMoves(cord, input):
    possibleMoves = []
    valueOfCord = input[cord[1]][cord[0]]
    for x in [1, 0, -1]:
        for y in [1, 0, -1]:
            if x == 0 and y == 0:
                continue
            if cord[0]-x < 0 or cord[1]-y < 0 or cord[0]-x > len(input[0])-1 or cord[1]-y > len(input)-1:
                continue
            if abs(x) == abs(y):
                continue
            
            if ord(input[cord[1]-y][cord[0]-x]) - ord(valueOfCord) == 1 or ord(input[cord[1]-y][cord[0]-x]) <= ord(valueOfCord):
                possibleMoves.append((cord[0]-x, cord[1]-y))
                
    return possibleMoves

def findGoal(nodesToSearch, shortestPathToCords, searchedNodes, input): 
    while(nodesToSearch != []):
        currentNode = nodesToSearch.pop(0)
        searchedNodes.append(currentNode)
        #print(shortestPathToCords[currentNode])
        possibleMoves = findPossibleMoves(currentNode, input)
        for move in possibleMoves:
            if move not in searchedNodes and move not in nodesToSearch:
                nodesToSearch.append(move)
            if shortestPathToCords[move] > shortestPathToCords[currentNode] + 1:
                shortestPathToCords[move] = shortestPathToCords[currentNode] + 1
    return shortestPathToCords

def partOne():
    input = parseInput()
    shortestPathToCords = {}
    nodesToSearch = []
    searchedNodes = []
    goalCords = (0, 0)
    for i, x in enumerate(input):
        for j, y in enumerate(x):
            if y == 'E':
                goalCords = (j,i)
                input[i] = input[i].replace("E","z")
            if y == 'S':
                nodesToSearch.append((j,i))
                input[i] = input[i].replace("S","a")
                shortestPathToCords[(j,i)] = 0
            else:
                shortestPathToCords[(j,i)] = 100000

    findGoal(nodesToSearch, shortestPathToCords, searchedNodes, input)
    print(shortestPathToCords[goalCords])

def findPossibleMovesPartTwo(cord, input):
    possibleMoves = []
    valueOfCord = input[cord[1]][cord[0]]
    for x in [1, 0, -1]:
        for y in [1, 0, -1]:
            if x == 0 and y == 0:
                continue
            if cord[0]-x < 0 or cord[1]-y < 0 or cord[0]-x > len(input[0])-1 or cord[1]-y > len(input)-1:
                continue
            if abs(x) == abs(y):
                continue
            
            if ord(valueOfCord) - ord(input[cord[1]-y][cord[0]-x]) == 1 or ord(input[cord[1]-y][cord[0]-x]) >= ord(valueOfCord):
                possibleMoves.append((cord[0]-x, cord[1]-y))
                
    return possibleMoves       
       
def findClosestA(nodesToSearch, shortestPathToCords, searchedNodes, input): 
    while(nodesToSearch != []):
        currentNode = nodesToSearch.pop(0)
        searchedNodes.append(currentNode)
        possibleMoves = findPossibleMovesPartTwo(currentNode, input)
        for move in possibleMoves:
            
            if move not in searchedNodes and move not in nodesToSearch:
                nodesToSearch.append(move)
            if shortestPathToCords[move] > shortestPathToCords[currentNode] + 1:
                
                shortestPathToCords[move] = shortestPathToCords[currentNode] + 1
    return shortestPathToCords

                    
def partTwo():
    input = parseInput()
    shortestPathToCords = {}
    nodesToSearch = []
    searchedNodes = []
    for i, x in enumerate(input):
        for j, y in enumerate(x):
            if y == 'E':
                input[i] = input[i].replace("E","z")
                nodesToSearch.append((j,i))
                shortestPathToCords[(j,i)] = 0
            else:
                shortestPathToCords[(j,i)] = 100000

    findClosestA(nodesToSearch, shortestPathToCords, searchedNodes, input)
    pathsToA = []
    for i, x in enumerate(input):
        for j, y in enumerate(x):
            if y == 'a':
                pathsToA.append(shortestPathToCords[(j,i)])
    print(min(pathsToA))
partOne()
partTwo()