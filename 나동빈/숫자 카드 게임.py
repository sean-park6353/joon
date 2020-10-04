m, n = map(int, input().split())

arr = []

for i in range(m):
    arr.append(list(map(int, input().split())))

num = 9000000
for i in arr:
    if min(i) < num:
