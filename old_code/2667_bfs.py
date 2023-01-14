from collections import deque
xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]
a = int(input())
graph = []
visit = [[False]*a for i in range(a)]
for i in range(a):
    graph.append(list(map(int, input().strip(' '))))


def bfs(m, n):
    cnt = 0
    q = deque([(m, n)])
    visit[m][n] = True  # 방문표시
    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x+xpos[i]
            new_y = y+ypos[i]
            if new_x >= a or new_y >= a or new_x < 0 or new_y < 0:
                continue
            if visit[new_x][new_y] == True:
                continue
            if graph[new_x][new_y] != 1:
                continue
            visit[new_x][new_y] = True
            q.append(((new_x, new_y)))
        cnt += 1
    return cnt


result = []
for i in range(a):
    for j in range(a):
        if visit[i][j] == 0 and graph[i][j] == 1:  # 방문하지 않았고 1인경우
            result.append(bfs(i, j))

result.sort()
print(len(result))
print(*result, sep='\n')
