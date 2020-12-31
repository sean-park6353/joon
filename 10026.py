# 합쳐보자!
import sys
sys.setrecursionlimit(50000)
xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]
n = int(input())
graph = []
visit = [[False]*n for i in range(n)]
for i in range(n):
    graph.append(list(map(str, input().strip(""))))


def dfs1(x, y):  # 일반인 버전 dfs
    visit[x][y] = True
    if graph[x][y] == 'R':
        for i in range(4):
            new_x = x+xpos[i]
            new_y = y+ypos[i]
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:  # 범위를 벗어나면
                continue
            if visit[new_x][new_y] == True:  # 이미 방문을 했다면
                continue
            if graph[new_x][new_y] != 'R':  # 빨강색일때 빨강색이 아니라면
                continue
            dfs1(new_x, new_y)

    elif graph[x][y] == 'G':
        for i in range(4):
            new_x = x+xpos[i]
            new_y = y+ypos[i]
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:  # 범위를 벗어나면
                continue
            if visit[new_x][new_y] == True:  # 이미 방문을 했다면
                continue
            if graph[new_x][new_y] != 'G':  # 빨강색일때 빨강색이 아니라면
                continue
            dfs1(new_x, new_y)
    else:
        for i in range(4):
            new_x = x+xpos[i]
            new_y = y+ypos[i]
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:  # 범위를 벗어나면
                continue
            if visit[new_x][new_y] == True:  # 이미 방문을 했다면
                continue
            if graph[new_x][new_y] != 'B':  # 빨강색일때 빨강색이 아니라면
                continue
            dfs1(new_x, new_y)


def dfs2(x, y):  # 색약용 버전 dfs
    visit[x][y] = True
    if graph[x][y] == 'R':
        for i in range(4):
            new_x = x+xpos[i]
            new_y = y+ypos[i]
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:  # 범위를 벗어나면
                continue
            if visit[new_x][new_y] == True:  # 이미 방문을 했다면
                continue
            if graph[new_x][new_y] == 'B':  # 빨강색일때 빨강색 혹은 초록색이 아니라면
                continue
            dfs2(new_x, new_y)
    elif graph[x][y] == 'G':
        for i in range(4):
            new_x = x+xpos[i]
            new_y = y+ypos[i]
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:  # 범위를 벗어나면
                continue
            if visit[new_x][new_y] == True:  # 이미 방문을 했다면
                continue
            if graph[new_x][new_y] == 'B':  # 빨강색일때 빨강색 혹은 초록색이 아니라면
                continue
            dfs2(new_x, new_y)
    else:
        for i in range(4):
            new_x = x+xpos[i]
            new_y = y+ypos[i]
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:  # 범위를 벗어나면
                continue
            if visit[new_x][new_y] == True:  # 이미 방문을 했다면
                continue
            if graph[new_x][new_y] != 'B':  # 빨강색일때 빨강색이 아니라면
                continue
            dfs2(new_x, new_y)


cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            cnt1 += 1
            dfs1(i, j)
visit = [[False]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            cnt2 += 1
            dfs2(i, j)
print(cnt1, cnt2)
