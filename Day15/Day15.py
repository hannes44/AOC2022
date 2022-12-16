import re
def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [re.split(",|:", line) for line in inputLines]
        for i,line in enumerate(inputLines):
            for j,word in enumerate(line):
                inputLines[i][j] = "".join(list(filter(lambda x: x.isnumeric() or x == "-" ,word)))
                inputLines[i][j] = int(inputLines[i][j])
        return inputLines

def calculateCordsWithoutBeaconsLine(sensorCords, closestBeaconCords, cordsWithoutBeacons, line = 10):
    manhattanDistanceToBeacon = abs(sensorCords[0] - closestBeaconCords[0]) + abs(sensorCords[1] - closestBeaconCords[1])
    yDistanceToLine = abs(sensorCords[1] - line)
    if sensorCords[1] + manhattanDistanceToBeacon < line or sensorCords[1] - manhattanDistanceToBeacon > line:
        return
    for x in range(-manhattanDistanceToBeacon, manhattanDistanceToBeacon):
        if abs(x) + yDistanceToLine > manhattanDistanceToBeacon:
            continue
        if (sensorCords[0] - x) == closestBeaconCords[0] and line == closestBeaconCords[1]:
            continue
        cordsWithoutBeacons[(sensorCords[0] - x, line)] = 0

def partOne():
    input = parseInput()
    cordsWithoutBeacons = {}
    
    for x in input:
        sensorCords = (x[0], x[1])
        beaconCords = (x[2], x[3])
        calculateCordsWithoutBeaconsLine(sensorCords, beaconCords, cordsWithoutBeacons)
    for x in input:
        beaconCords = (x[2], x[3])
        if beaconCords in cordsWithoutBeacons:
            del cordsWithoutBeacons[beaconCords]
    print(len(cordsWithoutBeacons))

class Rectangle():
    def __init__(self, centerCords, manhattanDistance):
        self.manhattanDistance = manhattanDistance
        self.centerCords = centerCords
    def isInsideRectangle(self, point):
        if abs(point[0] - self.centerCords[0]) + abs(point[1] - self.centerCords[1]) > self.manhattanDistance:
            return False

        return True

        
def calculateCordsWithoutBeacons(sensorCords, closestBeaconCords, rectangles, oneOffBorder, interval):
    manhattanDistanceToBeaconOneOff = abs(sensorCords[0] - closestBeaconCords[0]) + abs(sensorCords[1] - closestBeaconCords[1]) + 1 
    manhattanDistanceToBeacon = abs(sensorCords[0] - closestBeaconCords[0]) + abs(sensorCords[1] - closestBeaconCords[1])
    for x in range(manhattanDistanceToBeacon):
        if not (sensorCords[0] + x > interval or sensorCords[1] + manhattanDistanceToBeaconOneOff - x > interval):
            oneOffBorder.append((sensorCords[0] + x, sensorCords[1] + manhattanDistanceToBeaconOneOff - x))
        if not (sensorCords[0] + x > interval or sensorCords[1] - manhattanDistanceToBeaconOneOff + x > interval):
            oneOffBorder.append((sensorCords[0] + x, sensorCords[1] - manhattanDistanceToBeaconOneOff + x))
        if not (sensorCords[0] - x < 0 or sensorCords[1] + manhattanDistanceToBeaconOneOff - x > interval):
            oneOffBorder.append((sensorCords[0] - x, sensorCords[1] + manhattanDistanceToBeaconOneOff - x))
        if not (sensorCords[0] - x < 0 or sensorCords[1] - manhattanDistanceToBeaconOneOff + x > interval):
            oneOffBorder.append((sensorCords[0] - x, sensorCords[1] - manhattanDistanceToBeaconOneOff + x))
    rectangles.append(Rectangle(sensorCords, manhattanDistanceToBeacon))
        
def partTwo():
    input = parseInput()
    interval = 4000000
    rectangles = []
    oneOffBorder = []
    for x in input:
        sensorCords = (x[0], x[1])
        beaconCords = (x[2], x[3])
        calculateCordsWithoutBeacons(sensorCords, beaconCords, rectangles,oneOffBorder, interval)
    for x in oneOffBorder:
        found = False
        for y in rectangles:
            if y.isInsideRectangle(x):
                found = True
        if not found:
            print(x[0]*interval + x[1])
            return 

partOne()
partTwo()