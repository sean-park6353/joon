import sys

n = int(sys.stdin.readline())

arr = []
for j in range(n):
    arr.extend(list(map(int, sys.stdin.readline().rsplit())))

print(arr)
b = []
for i in range(0, int(2*n), 2):
    b.append(arr[i]+arr[i+1])


for i in range(n):
    print(b[i])
