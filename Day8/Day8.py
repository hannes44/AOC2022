def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [[int(x) for x in line.split(" ")[0]] for line in inputLines]
        return inputLines    

def partOne():
    input = parseInput()
    visibleCordinates = []
    print(input)
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if j == 0 or j == len(row)-1 or i == 0 or i == len(input)-1:
                visibleCordinates.append((i,j))
                continue
            if input[i][j] > max(row[0:j]):
                visibleCordinates.append((i,j))
            if input[i][j] > max(row[j+1:]):
                visibleCordinates.append((i,j))
            if input[i][j] > max([input[x][j] for x in range(len(input))][0:i]):
                visibleCordinates.append((i,j))
            if input[i][j] > max([input[x][j] for x in range(len(input))][i+1:]):
                visibleCordinates.append((i,j))
        
    print(len(set(visibleCordinates)))
def partTwo():
    input = parseInput()
    allScore = []
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            totalScoreForCord = 0
            currentValue = input[i][j]
            score = 0
            for y in reversed(row[0:j]):
                score += 1
                if y >= currentValue:
                    break
            totalScoreForCord += score
            score = 0
            for y in row[j+1:]:
                score += 1
                if y >= currentValue:
                    break
            totalScoreForCord *= score
            score = 0
            for y in reversed([input[x][j] for x in range(len(input))][0:i]):
                score += 1
                if y >= currentValue:
                    break
            totalScoreForCord *= score
            score = 0
            for y in [input[x][j] for x in range(len(input))][i+1:]:
                score += 1
                if y >= currentValue:
                    break
            totalScoreForCord *= score
            score = 0
            allScore.append(totalScoreForCord)
    print(max(allScore))
    
partOne()
partTwo()