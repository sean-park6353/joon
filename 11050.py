n, k = map(int, input().split(" "))


def func(n, k):
    if k == 0 or k == n:
        return 1
    if k > 0 and k < n:
        return func(n-1, k-1)+func(n-1, k)


print(func(n, k))
