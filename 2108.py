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
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
a = sum(arr)/n
b = arr.index(arr[int(len(arr)/2)-1])
print()
print(b)
