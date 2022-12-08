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

    
partOne()
partTwo()