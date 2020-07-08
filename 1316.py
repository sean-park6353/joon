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
            break
        else:
            g.append(arr[i])

for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == g[i][j+1]:  # 바로 옆에 붙어있는 경우
