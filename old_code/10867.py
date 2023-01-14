import sys
n = sys.stdin.readline()
arr = list(map(int, sys.stdin.readline().split(" ")))
arr = list(set(arr))
print(*sorted(arr), end=' ')
