import math

n = int(input())
for i in range(n):
    a, b = map(int, input().split(" "))
    if a == b:
        print(math.comb(a, b))
    else:
        print(math.comb(b, a))
