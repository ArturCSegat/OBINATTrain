from copy import copy

N = int(input())

g = {x+1: [] for x in range(N)}
for _ in range(N-1):
    row = [int(x) for x in input().split(" ")]
    g[row[0]].append(row[1])
    g[row[1]].append(row[0])

def max_distance_to_border(node: int, invalid=None, dist=0):
    if invalid is None:
        invalid = [node]
    
    best_end = 0
    best_value = 0
    for n in g[node]:
        if n in invalid: continue

        ninv = copy(invalid)
        ninv.append(n)
        value, end = max_distance_to_border(n, ninv, dist+1)
        #print(f"n: {n} (value, end): {(value, end)}")
        if value > best_value:
            best_value = value 
            best_end = end
    if best_end == 0:
        best_end = node
    else:
        dist = best_value

    return dist, best_end


largest = 0
pairs = []
count = 0

for x in g.keys():
    v, e = max_distance_to_border(x)
    if v > largest:
        pairs = [x*10+e, e*10+x]
        largest = v
        count = 1
    if v == largest:
        if x*10+e in pairs:
            continue
        count += 1
        pairs.append(x*10+e)
        pairs.append(e*10+x)

print(largest+1)
print(count)
    
