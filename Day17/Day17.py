import copy
def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [line.split(" ") for line in inputLines]
        return inputLines

def getPiece(index):
    if index == 0:
        return [[2,0],[3,0],[4,0],[5,0]]
    if index == 1:
        return [[2,1], [3,2],[3,1],[3,0],[4,1]]
    if index == 2:
        return [[2,0],[3,0], [4,0],[4,1],[4,2]]
    if index == 3:
        return [[2,3],[2,2],[2,1],[2,0]]
    if index == 4:
        return [[2,1],[2,0],[3,1],[3,0]]
    return -1

def partOne():
    input = parseInput()[0][0]
    print(input)
    board = [["." for i in range(7)] for j in range(7)]
    print(board)
    nextPiece = True
    pieceIndex = 0
    currentPiece = -1
    placesPieces = {}
    for x in range(7):
        placesPieces[(x,-1)] = True
    highestPiece = -1
    allRocksFallen = False
    rockCount = 0
    while(not allRocksFallen):
        for x in input:
            if allRocksFallen:
                break
            if nextPiece:
                currentPiece = getPiece(pieceIndex)
                pieceIndex += 1
                pieceIndex %= 5
                nextPiece = False
                for i, y in enumerate(currentPiece):
                    currentPiece[i][1] += highestPiece + 4
                    
            clearToPush = True
            if x == "<":
                if currentPiece[0][0] -1 >= 0:
                    for i in range(len(currentPiece)):
                        if (currentPiece[i][0] - 1, currentPiece[i][1]) in placesPieces:
                            clearToPush = False
                    if clearToPush:
                        for i in range(len(currentPiece)):
                            currentPiece[i] = [currentPiece[i][0]-1,currentPiece[i][1]]

            if x == ">":
                if currentPiece[-1][0] +1 <= len(board[0])-1:
                    for i in range(len(currentPiece)):
                        if (currentPiece[i][0] + 1, currentPiece[i][1]) in placesPieces:
                            clearToPush = False
                    if clearToPush:
                        for i in range(len(currentPiece)):
                            currentPiece[i] = [currentPiece[i][0]+1,currentPiece[i][1]]

            for y in currentPiece:
                if (y[0], y[1]-1) in placesPieces:
                    nextPiece = True
                    for j in currentPiece:
                        if j[1] > highestPiece:
                            highestPiece = j[1]
                        placesPieces[(j[0], j[1])] = True
                    rockCount += 1
                    if rockCount == 2022:
                        allRocksFallen = True   
                    break
                    
            for i, j in enumerate(currentPiece):
                currentPiece[i] = [j[0], j[1]-1]
                
    print(highestPiece + 1)
    
def partTwo():
    input = parseInput()[0][0]
    print(input)
    board = [["." for i in range(7)] for j in range(7)]
    print(board)
    nextPiece = True
    pieceIndex = 0
    currentPiece = -1
    placesPieces = {}
    for x in range(7):
        placesPieces[(x,-1)] = True
    highestPiece = -1
    allRocksFallen = False
    rockCount = 0
    topMostPieces = [-1,-1,-1,-1,-1,-1,-1]
    topMostPiecesAfterAllRocks = []
    
    print(len(input))
    count = 0
    while(not allRocksFallen):
        for x in input:
            if allRocksFallen:
                break
            if nextPiece:
                currentPiece = getPiece(pieceIndex)
                pieceIndex += 1
                pieceIndex %= 5
                nextPiece = False
                for i, y in enumerate(currentPiece):
                    currentPiece[i][1] += highestPiece + 4
                    
            clearToPush = True
            if x == "<":
                if currentPiece[0][0] -1 >= 0:
                    for i in range(len(currentPiece)):
                        if (currentPiece[i][0] - 1, currentPiece[i][1]) in placesPieces:
                            clearToPush = False
                            #print("< cant move")
                    if clearToPush:
                        for i in range(len(currentPiece)):
                            currentPiece[i] = [currentPiece[i][0]-1,currentPiece[i][1]]

            if x == ">":
                if currentPiece[-1][0] +1 <= len(board[0])-1:
                    for i in range(len(currentPiece)):
                        if (currentPiece[i][0] + 1, currentPiece[i][1]) in placesPieces:
                            clearToPush = False
                    if clearToPush:
                        for i in range(len(currentPiece)):

                            currentPiece[i] = [currentPiece[i][0]+1,currentPiece[i][1]]
            for y in currentPiece:
                if (y[0], y[1]-1) in placesPieces:
                    nextPiece = True
                    for j in currentPiece:
                        if j[1] > highestPiece:
                            highestPiece = j[1]
                        placesPieces[(j[0], j[1])] = True
                        if j[1] > topMostPieces[j[0]]:
                            topMostPieces[j[0]] = j[1]
                       # print(j)
                       
                    topPiecesDistances = [[],[],[],[],[],[],[]]
                    for k, g in enumerate(topMostPieces):
                        for b in range(len(topMostPieces)):
                            if k == b:
                                continue
                            topPiecesDistances[k].append(g-topMostPieces[b])
                    topMostPiecesAfterAllRocks.append(copy.deepcopy(topPiecesDistances))
                       
                       
                       
                    rockCount += 1
                    if rockCount == 2000:
                        allRocksFallen = True   

                    break

            for i, j in enumerate(currentPiece):
                currentPiece[i] = [j[0], j[1]-1]


    for i, x in enumerate(topMostPiecesAfterAllRocks):
        for k, y in enumerate(topMostPiecesAfterAllRocks):
            if i == k or i < k:
                continue
            if x == y:
                print(i - k)
                    

    # calculated answer by hand 
    # calculate cycle 
    # calculate after how many rocks cycle starts
    # calculate rocks after all cycles
    

partOne()
partTwo()