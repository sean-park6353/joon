n = int(input())
# cnt = list()
arr = []
for i in range(n):
    arr.append(input())
    # cnt.append(0)

g = []
c = 0
for i in range(n):
    for j in range(len(arr[i])):
        if arr[i].count(arr[i][j]) == 1:
            c = c+1
        else:
            g.append(arr[i])
            break

r = []
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i].count(g[i][j]) >= 2:
            r.append(g[i][j])
            break

for i in ra
