from sys import stdin
from sys import stdout

n = int(stdin.readline())
arr = []

for i in range(n):
    arr.append(stdin.readline())


arr = sorted(arr)

for i in range(n):
    stdout.write(arr[i])
