with open("inputdayseven.txt") as commandFile:
    commandFile.readline()
    root = {}
    currentDir = root
    currentDirPath = []
    for line in commandFile.readlines():
        line = line.replace("\n", "")
        if line[0] == "$":
            if line[2] == "c":
                command = line.replace("$ cd ", "")
                if command == "/":
                    currentDir = root
                    currentDirPath = []
                elif command == "..":
                    currentDirPath.pop()
                    currentDir = root
                    for dir in currentDirPath:
                        currentDir = currentDir[dir]
                else:
                    currentDir = currentDir[command]
                    currentDirPath.append(command)
        else:
            if line[0] == "d":
                dir = line.replace("dir ", "")
                currentDir[dir] = {}
            else:
                size, filename = line.split(" ")
                currentDir[filename] = int(size)
sum = 0
free = 70000000 - 46975962
need = 30000000 - free
vals = []
def sumDirectory(directory):
    global sum
    cSum = 0
    for item in directory.values():
        if isinstance(item, int):
            cSum += item
        else:
            cSum += sumDirectory(item)
    if cSum >= need:
        vals.append(cSum)
    return cSum

print(sumDirectory(root))
print(min(vals))
print(sum)