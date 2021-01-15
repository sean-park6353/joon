graph = [

    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 1, 1]

]
xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]


def dfs(x, y):
    visit[x][y] = True
    for i in range(4):
        new_x = x+xpos[i]
        new_y = y+ypos[i]
        if new_x < 0 or new_y < 0 or new_x >= 4 or new_y >= 4:
            continue
        if visit[new_x][new_y] == True:
            continue
        if graph[new_x][new_y] != 1:
            continue
        dfs(new_x, new_y)


visit = [[False]*4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        if graph[i][j] == 1 and visit[i][j] == False:
            dfs(i, j)
