from sys import stdin
from sys import stdout
n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))

# print(arr)
arr.sort()

for i in arr:
    print(' '.join(map(str, i)))

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] < arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# arr.reverse()
# for i in arr:
#     print(' '.join(map(str, i)))
