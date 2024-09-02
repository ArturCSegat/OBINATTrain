from copy import copy
[N, M] = [int(x) for x in input().split(" ")]

circulo = {x+1: [] for x in range(N)}
quadrado = {x+1: [] for x in range(M)}

for _ in range(N-1):
    row = [int(x) for x in input().split(" ")]
    circulo[row[0]].append(row[1])
    circulo[row[1]].append(row[0])
for _ in range(M-1):
    row = [int(x) for x in input().split(" ")]
    quadrado[row[0]].append(row[1])
    quadrado[row[1]].append(row[0])

def find(start, end, g:dict[int, list[int]], path=None):
    if path is None:
        path =[]

    path.append(start)
    for n in g[start]:
        if n in path: continue
        if n == end:
            path.append(n)
            return path
        if find(n, end, g, path):
            return path
    path.pop()
    return None
        
def diameter(g):
    return max([find(x, y, g) for y in g.keys() for x in g.keys()], key=lambda x:len(x) if x is not None else 0)


median = lambda x: x[len(x)//2]

print(f"{median(diameter(circulo))} {median(diameter(quadrado))}")




