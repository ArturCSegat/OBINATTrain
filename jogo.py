[L, C] = [int(x) for x in input().split(" ")]
P = int(input())

WHITE = 1
BLACK = 2

board = [[0 for _ in range(C)] for _ in range(L)]

valid = lambda x,y: x < L and x >= 0 and y < C and y >= 0

ns = [(-1,0),(0,-1),(0,1),(1,0)]
def has_white_neighbours(x, y) -> bool:
    for n in ns:
        if not valid(x+n[0], y+n[1]):
            continue

        p = board[x+n[0]][y+n[1]]
        if p == WHITE:
            return True
    return False

counter = 0
for _ in range(P):
    row = [int(x) for x in input().split(" ")]
    x = (row[0]-1)
    y = (row[1]-1)

    board[x][y] = BLACK

    for n in ns:
        if not valid(x+n[0], y+n[1]):
            continue

        p = board[x+n[0]][y+n[1]]
        if p == WHITE:
            continue

        if not has_white_neighbours(x+n[0],  y+n[1]):
            counter += 1
            board[x+n[0]][y+n[1]] = WHITE

print(counter)

