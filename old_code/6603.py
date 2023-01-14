
from itertools import combinations
n = []
arr = []
while True:
    n = list(map(int, input().split()))
    arr.append(n)
    if sum(n) == 0:
        arr.pop()
        break
for i in range(len(arr)):
    arr[i].remove(arr[i][0])

for i in range(len(arr)):
    arr[i].sort()
result = []

for i in range(len(arr)):
    result.append(list(combinations(arr[i], 6)))

for i in range(len(result)):
    for j in range(len(result[i])):
        print(" ".join(map(str, result[i][j])))
    if i != len(result)-1:
        print()


# a = [8, 9, 10, 12, 4, 14, 49]
# a.sort()
# print(list(combinations(a, 6)))
