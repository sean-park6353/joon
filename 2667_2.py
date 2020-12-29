
xpos = [-1, 1, 0, 0]  # 상하좌우
ypos = [0, 0, -1, 1]  # 상하좌우

cnt = 0


def dfs(a, b):
    global cnt
    visit[a][b] = True
    cnt += 1
    for i in range(4):
        x = a+xpos[i]
        y = b+ypos[i]
        if x >= n or y >= n or x < 0 or y < 0:
            continue
        if graph[x][y] != 1:
            continue
        if visit[x][y] == True:
            continue

        dfs(x, y)


n = int(input())
graph = []

result = []
for i in range(n):
    graph.append(list(map(int, input().strip(''))))
visit = [[False] * n for i in range(n)]
x = 0
y = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visit[i][j] == False:  # ! 방문이 안 되고 연결이 되어있으면
            dfs(i, j)
            result.append(cnt)
            cnt = 0

print(len(result))
print(*result, sep='\n')
