[E, V] = [int(x) for x in input().split(" ")]
g = {i: [] for i in range(1, E+1)}

for _ in range(V):
    row = [int(x) for x in input().split(" ")]
    g[row[0]].append((row[1], row[2]))
    g[row[1]].append((row[0], row[2]))


def DFS(start, end, train_len, occupied=None, cost=0, last=0) -> int:
    removed = []
    if occupied is None:
        occupied = []

    if cost >= train_len:
        removed.append(occupied.pop(0))

    if start in occupied:
        for r in removed:
            occupied.insert(0, r)
        return -1

    if start == end and last != 0:
        return cost

    occupied.append(start)

    for (node, cost_to) in g[start]:
        if node == last:
            continue
        r = DFS(node, end, train_len, occupied, cost+cost_to, last=start)
        if r != -1:
            return r
        
    occupied.pop()
    for r in removed:
        occupied.insert(0, r)
    
    return -1

for _ in range(int(input())):
    row = [int(x) for x in input().split()]
    print(DFS(row[0], row[0], row[1]))

