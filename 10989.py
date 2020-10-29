from sys import stdin
from sys import stdout

n = int(stdin.readline())
arr = []
result = [0]*10000
for i in range(n):
    arr.append(stdin.readline())
    result[arr[i]] += 1

print(result)


# for i in range(n):
#     stdout.write(arr[i])
