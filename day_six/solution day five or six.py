def partOne():
    with open("inputdayfiveorsix.txt") as file:
        line = file.readline()
        for i in range(len(line)):
            area = line[i : i + 14]
            print(area)
            setArea = set(area)
            print(setArea)
            print(len(setArea))
            print(i)
            if len(setArea) == 14:
                return i + 15
print(partOne())
            
