[N, M] = [int(x) for x in input().split(" ")] 
S = [int(x) for x in input().split(" ")]

def mds(s: list[int], e: int, d:int) -> int:
    best = min([s[i] for i in range(e, d)])
    if best <= 1:return best
    while True:
        if sum([s[i] % best for i in range(e, d)]) != 0:
            best -= 1
        else:
            return best

for _ in range(M):
    row = [int(x) for x in input().split(" ")]

    if row[0] == 1:
        S[row[1]-1] = row[2]
    if row[0] == 2:
        start = row[1] - 1
        end = row[2] - 1

        counter = 0
        sub_len = (end - start)+ 1
        for window_len in range (1, sub_len+1):
            for i in range(sub_len - window_len + 1):
                if window_len == 1 and S[start+i] != 1:
                    counter+=1
                    continue

                if mds(S, start+i, start+i+window_len) > 1:
                    counter += 1
        print(counter)
