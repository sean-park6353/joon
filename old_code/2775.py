T = int(input())


def func(k, n):
    arr = []
    if k == 0:
        return int(n*(n+1)/2)
    for i in range(1, n+1):
        arr.append(func(k-1, i))
    return arr


for i in range(1, T+1):
    k = int(input())
    n = int(input())
    arr = func(k, n)
