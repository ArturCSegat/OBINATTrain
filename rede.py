N = int(input())

msgs = [int(input()) for _ in range(N)]

largest = 0
for i in range(1, N+1):
    count = sum(1 for m in msgs if m >= i)
    if count >= i and i > largest:
        largest = i 
print(largest)