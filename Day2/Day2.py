from enum import Enum
def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [line.split(" ") for line in inputLines]
        return inputLines
    
class Hand(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3
    
def charToHand(char):
    if char == "A" or char == "X":
        return Hand.Rock
    if char == "B" or char == "Y":
        return Hand.Paper
    if char == "C" or char == "Z":
        return Hand.Scissors

def partOne():
    WIN = 6
    TIE = 3
    input = parseInput()
    input = [[charToHand(x),charToHand(y)] for [x, y] in input]
    
    totalPoints = 0
    for game in input:
        player = game[1]
        opponent = game[0]
        
        totalPoints += player.value
        if player == opponent:
            totalPoints += TIE
        if player == Hand.Rock:
            if opponent == Hand.Scissors:
                totalPoints += WIN
        if player == Hand.Paper:
            if opponent == Hand.Rock:
                totalPoints += WIN
        if player == Hand.Scissors:
            if opponent == Hand.Paper:
                totalPoints += WIN

    print(totalPoints)
def partTwo():
    WIN = 6
    TIE = 3 
    INDICATEDWIN = 3
    INDICATEDTIE = 2
    INDICATEDLOSS = 1
    input = parseInput()
    input = [[charToHand(x),charToHand(y)] for [x, y] in input]
    
    totalPoints = 0
    for game in input:
        player = game[1]
        opponent = game[0]
        if opponent == Hand.Rock:
            if player.value == INDICATEDWIN:
                totalPoints += WIN + Hand.Paper.value
            if player.value == INDICATEDTIE:
                totalPoints += TIE + Hand.Rock.value
            if player.value == INDICATEDLOSS:
                totalPoints += Hand.Scissors.value
        if opponent == Hand.Paper:
            if player.value == INDICATEDWIN:
                totalPoints += WIN + Hand.Scissors.value
            if player.value == INDICATEDTIE:
                totalPoints += TIE + Hand.Paper.value
            if player.value == INDICATEDLOSS:
                totalPoints += Hand.Rock.value
        if opponent == Hand.Scissors:
            if player.value == INDICATEDWIN:
                totalPoints += WIN + Hand.Rock.value
            if player.value == INDICATEDTIE:
                totalPoints += TIE + Hand.Scissors.value
            if player.value == INDICATEDLOSS:
                totalPoints += Hand.Paper.value    

    print(totalPoints)
partOne()
partTwo()
