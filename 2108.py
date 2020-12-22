# from sys import stdin
# from sys import stdout
# n = int(stdin.readline())
# coll
# arr = []
# for i in range(n):
#     arr.append(int(stdin.readline()))
# arr.sort()
# stdout.write(str(round(sum(arr)/n)))
# stdout.write('\n')
# stdout.write(str(arr[arr.index((int(max(arr)+min(arr)/2)))]))
# stdout.write('\n')
# big = arr[0]
# for i in arr:
#     if big < arr.count(i):
#         big = i
# stdout.write(str(big))
# stdout.write('\n')
# stdout.write(str(max(arr)-min(arr)))

import math


def roundUp(num):
    if num >= 0:
        return int(num) + 1 if (num - int(num)) >= 0.5 else int(num)
    else:
        num = abs(num)
        return -int(num) + 1 if (num - int(num)) >= 0.5 else int(num)


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
a = roundUp(sum(arr)/n)
b = arr.index(arr[len(arr)//2])
big = 0
for i in arr:
    if arr.count(i) > big:
        big = i
c = big

print(a)
print(b)
print(c)
