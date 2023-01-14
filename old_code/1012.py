import sys
sys.setrecursionlimit(50000)
t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j, m, n):
    visited[i][j] = True
    for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]
        if ni >= n or nj >= m or ni < 0 or nj < 0:
            continue
        if visited[ni][nj] == True:
            continue
        if arr[ni][nj] != 1:
            continue
        dfs(ni, nj, m, n)


for tc in range(t):
    cnt = 0
    visited = []
    pos = []
    arr = []
    m, n, k = map(int, input().split(' '))
    for i in range(n):
        arr.append([0]*m)
        visited.append([False]*m)
    for i in range(k):
        a, b = map(int, input().split(' '))
        arr[b][a] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == False:
                dfs(i, j, m, n)
                cnt += 1
    print(cnt, end='\n')
