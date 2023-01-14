

def func(n):
    if n > 1:
        return n*func(n-1)
    else:
        return 1


a = int(input())
print(func(a))
