[N, M] = [int(x) for x in input().split(" ")]

g = {x+1: [] for x in range(N)}

def find(start_node: int, end_node: int):
    for n in g[start_node]:
        if n == end_node:
            return True
        if find(n, end_node):
            return True

    return False

for i in range(M):
    row = [int(x) for x in input().split(" ")]
    start = row[0]
    for r in range(row[1], row[2]+1):
        g[start].append(r)
    for k in g.keys():
        if find(k, k):
            print(i+1)
            exit()

print(-1)
