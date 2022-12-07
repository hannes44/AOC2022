class Folder():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

def traverseTree(folder, sum, allFolders):
    folderSize = 0
    for x in folder.get_children():
        if x.size == 0:
            folderSize += traverseTree(x, sum, allFolders)
        else:    
            folderSize += x.size
    folder.size = folderSize
    if folderSize <= 100000:
        sum[0] += folderSize

    allFolders.append(folderSize)
    return folderSize
    

def parseInput():
    with open("input.txt", "r") as f:
        input = f.readlines()
        inputLines = [line.strip() for line in input]
        inputLines = [line.split(" ") for line in inputLines]
        return inputLines

def partOne():
    input = parseInput()
    topMostFolder = Folder("GigaFolder", None)
    currentFolder = topMostFolder
    addingToCurrentFolder = False
    for x in input:
        if x[0] == '$':
            addingToCurrentFolder = False
            if x[1] == "cd":
                if x[2] == "/":
                    currentFolder = topMostFolder
                    continue
                elif x[2] == "..":
                    currentFolder = currentFolder.get_parent()
                    continue
                else:
                    currentFolder = list(filter(lambda y: y.name == x[2], currentFolder.get_children() ))[0]
            if x[1] == "ls":
                addingToCurrentFolder = True
                continue
        if addingToCurrentFolder:
            # if folder
            if x[0] == "dir":
                currentFolder.add_child(Folder(x[1], currentFolder))
            else:
                # if file
                newChild = Folder(x[1], currentFolder)
                newChild.size = int(x[0])
                currentFolder.add_child(newChild)
    sum = [0]
    traverseTree(topMostFolder, sum, [])
    print(sum[0])
    
def partTwo():
    input = parseInput()
    topMostFolder = Folder("GigaFolder", None)
    currentFolder = topMostFolder
    addingToCurrentFolder = False
    for x in input:
        if x[0] == '$':
            addingToCurrentFolder = False
            if x[1] == "cd":
                if x[2] == "/":
                    currentFolder = topMostFolder
                    continue
                elif x[2] == "..":
                    currentFolder = currentFolder.get_parent()
                    continue
                else:
                    currentFolder = list(filter(lambda y: y.name == x[2], currentFolder.get_children() ))[0]
            if x[1] == "ls":
                addingToCurrentFolder = True
                continue
            
        if addingToCurrentFolder:
            # if folder
            if x[0] == "dir":
                currentFolder.add_child(Folder(x[1], currentFolder))
            else:
                # if file
                newChild = Folder(x[1], currentFolder)
                newChild.size = int(x[0])
                currentFolder.add_child(newChild)
    sum = [0]
    sizeNeeded = 30000000 - (70000000 - 40913445)
    allFolders = []
    traverseTree(topMostFolder, sum, allFolders)
    allFolders = filter(lambda x: x >= sizeNeeded ,allFolders)
    print(min(allFolders))
    
partOne()
partTwo()