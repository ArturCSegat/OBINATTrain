import math

azul = int(input())
branco = int(input())
total = azul + branco

sq = math.sqrt(total)
if int(sq) == sq:
    print(f"{sq} {sq}")
    exit()

b = ((azul * total) / (2 * total) + 2) - 4
a = total / b

if int(a) != a or int(b) != b or a*b == (2*a)+(2*b)-4:
    print("-1 -1")
    exit()

print(f"{min(a, b)} {max(a, b)}")
