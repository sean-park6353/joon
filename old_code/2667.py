n = int(input())
arr = []
visited = []
cnt = 0
dan = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j):
    global cnt
    cnt += 1
    visited[i][j] = True
    for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]
        if ni < 0 or nj < 0 or nj >= n or ni >= n:
            continue
        if visited[ni][nj] == True:
            continue
        if arr[ni][nj] != 1:
            continue
        dfs(ni, nj)


for i in range(n):
    arr.append(list(map(int, input())))
    visited.append([False]*n)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == False:
            cnt = 0
            dfs(i, j)
            dan.append(cnt)

dan.sort()
print(len(dan))
for i in dan:
    print(i)
# print(cnt)
# print(dan)
# print(arr)
# print(visited)
