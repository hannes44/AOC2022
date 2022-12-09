def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [line.split(" ") for line in inputLines]
        return inputLines
    
def findMove(cordToMove, cord):
    for x in [1,0,-1]:
        for y in [1,0,-1]:
            if abs(cordToMove[0] + x - cord[0]) <= 1 and abs(cordToMove[1] + y - cord[1]) == 0:
                return (cordToMove[0]+x, cordToMove[1]+y)
            if abs(cordToMove[0] + x - cord[0]) == 0 and abs(cordToMove[1] + y - cord[1]) <= 1:
                return (cordToMove[0]+x, cordToMove[1]+y)
     
def findMovePartTwo(cordToMove, cord):
    for x in [1,0,-1]:
        for y in [1,0,-1]:
            if abs(cordToMove[0] + x - cord[0]) <= 1 and abs(cordToMove[1] + y - cord[1]) <= 1:
                return (cordToMove[0]+x, cordToMove[1]+y)
                                         
    
def partOne():
    input = parseInput()
    headCordinates = (0,0)
    tailCordinates = (0,0)
    visitedCoordinates = []
    for x in input:
        for y in range(0, int(x[1])):
            if x[0] == 'U':
                headCordinates = (headCordinates[0], headCordinates[1] + 1)
            if x[0] == 'D':
                headCordinates = (headCordinates[0], headCordinates[1] - 1)
            if x[0] == 'L':
                headCordinates = (headCordinates[0] - 1, headCordinates[1])
            if x[0] == 'R':
                headCordinates = (headCordinates[0] + 1, headCordinates[1])
            if abs(headCordinates[0]-tailCordinates[0]) > 1 or abs(headCordinates[1]-tailCordinates[1]) > 1:
                tailCordinates = findMove(tailCordinates, headCordinates)
            visitedCoordinates.append(tailCordinates)
    print(len(set(visitedCoordinates)))
             

                
def partTwo():
    input = parseInput()
    allHeadCordinates = [(0,0) for x in range(0,10)]
    allTailCordinates = [(0,0) for x in range(0,10)]
    visitedCoordinates = []
    
    for x in input:
        for y in range(0, int(x[1])):
            for j in range(0, 9):
                headCordinates = allHeadCordinates[j]
                tailCordinates = allTailCordinates[j]
                if j == 0:
                    if x[0] == 'U':
                        headCordinates = (headCordinates[0], headCordinates[1] + 1)
                    if x[0] == 'D':
                        headCordinates = (headCordinates[0], headCordinates[1] - 1)
                    if x[0] == 'L':
                        headCordinates = (headCordinates[0] - 1, headCordinates[1])
                    if x[0] == 'R':
                        headCordinates = (headCordinates[0] + 1, headCordinates[1])
                if abs(headCordinates[0]-tailCordinates[0]) > 1 and abs(headCordinates[1]-tailCordinates[1]) > 1:
                    tailCordinates = findMovePartTwo(tailCordinates, headCordinates)
                elif abs(headCordinates[0]-tailCordinates[0]) > 1 or abs(headCordinates[1]-tailCordinates[1]) > 1:
                    tailCordinates = findMove(tailCordinates, headCordinates)
                if j == 0:
                    allHeadCordinates[0] = headCordinates

                allHeadCordinates[j+1] = tailCordinates
                allTailCordinates[j] = tailCordinates
                if j == 8:
                    visitedCoordinates.append(tailCordinates)
    print(len(set(visitedCoordinates)))
                 
partOne()
partTwo()