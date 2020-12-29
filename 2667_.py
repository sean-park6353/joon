n = int(input())
arr = []
cnt = 0
dan = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[False]*n for i in range(n)]
for i in range(n):
    arr.append(list(map(int, input())))


def dfs(i, j):
    global cnt
    visit[i][j] = True
    cnt += 1
    for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]
        if ni < 0 or nj < 0 or ni >= n or nj >= n:
            continue
        if arr[ni][nj] != 1:
            continue
        if visit[ni][nj] == True:
            continue
        dfs(ni, nj)


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visit[i][j] == False:
            cnt = 0
            dfs(i, j)
            dan.append(cnt)

print(len(dan))
for i in dan:
    print(i, end='\n')
