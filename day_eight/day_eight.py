vis = 0
with open("input.txt") as iFile:
    grid = [[int(x) for x in line if x != "\n"] for line in iFile.readlines()]
    """grid = [[1,1,1,1,1],
            [1,2,2,2,1],
            [1,2,3,2,1],
            [1,2,2,2,1],
            [1,1,1,1,1],
    ]"""
    height = len(grid)
    width = len(grid[0])
    
    highestCols = [-1] * width
    colsSoFar = [[] for _ in range(width)]

    counted = [set() for _ in range(width)]

    for y, row in enumerate(grid):
        heighestRow = -1
        rowSoFar = []
        for x, tree in enumerate(row):
            toAdd = 0
            if tree > heighestRow:
                toAdd = 1
                heighestRow = tree
            if tree > highestCols[x]:
                toAdd = 1
                highestCols[x] = tree

            #rowSoFar = [x for x in rowSoFar if x > tree]
            #rowSoFar.append(tree)

            while rowSoFar and rowSoFar[-1][0] <= tree:
                rowSoFar.pop()

            while colsSoFar[x] and colsSoFar[x][-1][0] <= tree:
                colsSoFar[x].pop()
            
            #tree height, score, position
            rowSoFar.append((tree, 1 - toAdd, x))
            colsSoFar[x].append((tree, 1 - toAdd, y))
            #if toAdd:
            #    print(f"Counted {tree, x, y}")
            vis += toAdd

        for treeC in rowSoFar:
            vis += treeC[1]
            if treeC[1]:
                x = treeC[2]
                counted[x].add(y)
                #print(f"Counted {treeC[0], x, y}")

    for x, col in enumerate(colsSoFar):
        for treeC in col:
            if treeC[1]:
                y = treeC[2]
                if y not in counted[x]:
                    #print(f"Counted {treeC[0], x, y}")
                    vis += 1



print(vis)
