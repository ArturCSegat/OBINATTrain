N = int(input())

users = [0 for _ in range(N)]
counter = 0


for i in range(N):
    users[i] = input()

for i, u in enumerate(users):
    for j, other in enumerate(users):
        if j==i: continue
        if u in other: counter+=1

print(counter)
