import copy
a, b = map(int, input().split(' '))

xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]
graph = []
for i in range(a):
    graph.append(list(map(str, input().strip(""))))
visit = [[False]*b for _ in range(a)]


def dfs(x, y):
    visit[x][y] = True
    for i in range(4):
        new_x = x+xpos[i]
        new_y = y+ypos[i]
        if new_x < 0 or new_y < 0 or new_x >= a or new_y >= b:
            continue
        if visit[new_x][new_y] == True:
            continue
        if graph[new_x][new_y] != '#':
            continue
        dfs(new_x, new_y)


cnt = 0
for i in range(a):
    for j in range(b):
        if graph[i][j] == '#' and visit[i][j] == False:
            cnt += 1
            dfs(i, j)
print(cnt)
