moves = {"U" : (0, 1),
             "L" : (-1, 0),
             "R" : (1, 0),
             "D" : (0, -1)}
def sign(num):
    if num > 0:
        return 1
    if num == 0:
        return 0
    return -1
"""with open("input.txt") as iFile:
    hX, hY = 0, 0
    tX, tY = 0, 0
    visited = set()
    visited.add((tX, tY))

    

    for line in iFile.readlines():
        line = line.strip()
        move, amount = line.split(" ")
        xMove, yMove = moves[move]
        for _ in range(int(amount)):
            hX += xMove
            hY += yMove
            dis = ((hX - tX) **2 + (hY - tY) ** 2) ** 0.5
            if dis >= 2:
                if hX == tX:
                    tY += sign(hY - tY)
                elif hY == tY:
                    tX += sign(hX - tX)
                else:
                    tX += sign(hX - tX)
                    tY += sign(hY - tY)
                visited.add((tX, tY))
    print(len(visited))
"""

with open("input.txt") as iFile:
    class Knot:
        def __init__(self, head, x = 0, y = 0) -> None:
            self.head = head
            self.x = x
            self.y = y
        def disBetween(self, other):
            return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        def __sub__(self, other):
            return self.x - other.x, self.y - other.y
        def __iadd__(self, other):
            self.x += sign(other[0])
            self.y += sign(other[1])
            return self
        def move(self):
            if self.disBetween(self.head) >= 2:
                self += self.head - self
        def pos(self):
            return self.x, self.y
        def __str__(self):
            return f"{self.x} {self.y} {self.disBetween(self.head)}"
    head = Knot(None)
    tails = []
    prev = head
    visited = set()
    for _ in range(9):
        tails.append(Knot(prev))
        prev = tails[-1]
    for line in iFile.readlines():
        line = line.strip()
        move, amount = line.split(" ")
        move = moves[move]
        pass
        for _ in range(int(amount)):
            head += move
            for tail in tails:
                tail.move()
            visited.add(prev.pos())
    print(len(visited))

