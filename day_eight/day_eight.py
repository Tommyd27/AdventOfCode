#Part A:
"""with open("input.txt") as iFile:
    vis = 0
    grid = [[int(x) for x in line if x != "\n"] for line in iFile.readlines()]

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


            while rowSoFar and rowSoFar[-1][0] <= tree:
                rowSoFar.pop()

            while colsSoFar[x] and colsSoFar[x][-1][0] <= tree:
                colsSoFar[x].pop()
            
            rowSoFar.append((tree, 1 - toAdd, x))
            colsSoFar[x].append((tree, 1 - toAdd, y))
            vis += toAdd

        for treeC in rowSoFar:
            vis += treeC[1]
            if treeC[1]:
                x = treeC[2]
                counted[x].add(y)

    for x, col in enumerate(colsSoFar):
        for treeC in col:
            if treeC[1]:
                y = treeC[2]
                if y not in counted[x]:
                    vis += 1
    print(vis)"""

#Part B:
with open("input.txt") as iFile:
    grid = [[int(x) for x in line if x != "\n"] for line in iFile.readlines()]
    height = len(grid)
    width = len(grid[0])
    maxViewingScore = 0

    def findViewingScore(x, y, tree):
        def findDirectionScore(x1, y1, direction):
            if not (0 <= x1 < width and 0 <= y1 < height):
                return 0
            if grid[x1][y1] >= tree:
                return 1
            return 1 + findDirectionScore(x1 + direction[0], y1 + direction[1], direction) 
        viewingScore = 1
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            viewingScore *= findDirectionScore(x + direction[0], y + direction[1], direction)
        return viewingScore
        
    for y, row in enumerate(grid):
        for x, tree in enumerate(row):
            viewingScore = findViewingScore(x, y, tree)
            print(f"{x} {y} {viewingScore}")
            maxViewingScore = max(maxViewingScore, viewingScore)
    print(maxViewingScore)
