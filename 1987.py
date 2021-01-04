xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]
a, b = map(int, input().split(" "))
graph = []
visit = []
archive = []
cnt = 1
result = []
visit = [[False]*b for i in range(a)]
for i in range(a):
    graph.append(list(map(str, input().strip(""))))


def dfs(x, y):
    global cnt
    visit[x][y] = True  # 방문처리
    archive.append(graph[x][y])  # 아카이브에 추가
    for i in range(4):
        new_x = x+xpos[i]
        new_y = y+ypos[i]
        if new_x >= a or new_y >= b or new_x < 0 or new_y < 0:  # 범위를 초과한다면
            continue
        if visit[new_x][new_y] == True:  # 방문했다면
            continue
        if graph[new_x][new_y] in archive:  # 현재 알파벳이 아카이브에 있다면
            result.append(cnt)
            continue
        cnt += 1
        dfs(new_x, new_y)
    archive.clear()


dfs(0, 0)
print(cnt)
print(result)
