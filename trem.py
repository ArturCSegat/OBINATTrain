[E, V] = [int(x) for x in input().split(" ")]
g = {i: [] for i in range(1, E+1)}

for _ in range(V):
    row = [int(x) for x in input().split(" ")]
    g[row[0]].append((row[1], row[2]))
    g[row[1]].append((row[0], row[2]))


def DFS(start: int, end: int, cost=0, vis=None) -> int:
    if vis is None:
        vis = []
    
    if start == end and len(vis) > 2:
        return cost

    if start in vis:
        return -1

    vis.append(start)

    for (node, cost_to) in g[start]:
        r = DFS(node, end, cost+cost_to, vis)
        if r != -1:
            return r 
        
    vis.pop()
    return -1

print()
print()

for _ in range(int(input())):
    row = [int(x) for x in input().split()]
    print(DFS(row[0], row[0]))

