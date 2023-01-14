import sys
sys.setrecursionlimit(50000)
xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]
a = int(input())


def dfs(x, y, n):
    visit[x][y] = True
    for i in range(4):
        new_x = x+xpos[i]
        new_y = y+ypos[i]
        if new_x >= a or new_y >= a or new_x < 0 or new_y < 0:
            continue
        if visit[new_x][new_y] == True:
            continue
        if graph[new_x][new_y]-n <= 0:
            continue
        dfs(new_x, new_y, n)


graph = []
result = []
visit = [[False]*a for i in range(a)]

for i in range(a):
    graph.append(list(map(int, input().split(' '))))
    answer = max(graph[i])

for k in range(answer, -1, -1):
    visit = [[False]*a for i in range(a)]
    cnt = 0

    for i in range(a):
        for j in range(a):
            if visit[i][j] == False and graph[i][j]-k > 0:
                dfs(i, j, k)
                cnt += 1
    result.append(cnt)

print(max(result))
