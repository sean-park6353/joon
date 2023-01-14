from sys import stdin
n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(len(arr)):
    arr[i].reverse()


print(type(arr))
arr.sort()
for i in range(len(arr)):
    arr[i].reverse()
for i in arr:
    print(' '.join(map(str, i)))
