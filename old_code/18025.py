

n = int(input())
arr = list(map(int, input().split(' ')))


def MoreBigger(a, b):
    if a >= b:
        return a
    else:
        return b


index = 0
result = MoreBigger(arr[0], arr[2])
for i in range(len(arr)-2):
    tmp = MoreBigger(arr[i], arr[i+2])
    if tmp < result:
        result = tmp
        index = i


print(index+1, result)
