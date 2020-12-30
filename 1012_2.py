t = int(input())
xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]


def dfs(x, y):
    visit[x][y] = True
    for i in range(4):
        new_x = x+xpos[i]
        new_y = y+ypos[i]
        if new_x < 0 or new_y < 0 or new_x >= b or new_y >= a:
            continue
        if visit[new_x][new_y] == True:
            continue
        if graph[new_x][new_y] != 1:
            continue
        dfs(new_x, new_y)


result = []

for i in range(t):
    cnt = 0
    a, b, n = map(int, input().split(" "))
    graph = [[0]*a for p in range(b)]
    visit = [[False]*a for p in range(b)]
    for j in range(n):
        data = list(map(int, input().split(' ')))
        graph[data[1]][data[0]] = 1
    for j in range(b):
        for k in range(a):
            if graph[j][k] == 1 and visit[j][k] == False:  # 배추가 있다면
                dfs(j, k)
                cnt += 1
    print(cnt)
