from collections import deque
xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]
a, b = map(int, input().split(' '))
visit = [[0]*b for _ in range(a)]
graph = []
for i in range(a):
    graph.append(list(map(int, input().strip(' '))))


def bfs(x, y):
    q = deque([(x, y)])
    visit[x][y] = 1
    while q:
        m, n = q.popleft()
        if m == a-1 and n == b-1:
            return visit[m][n]
        for i in range(4):
            new_x = m+xpos[i]
            new_y = n+ypos[i]
            if new_x >= a or new_y >= b or new_x < 0 or new_y < 0:
                continue
            if visit[new_x][new_y] != 0:
                continue
            if graph[new_x][new_y] != 1:
                continue
            visit[new_x][new_y] = visit[m][n]+1
            q.append((new_x, new_y))
    return visit[m][n]


print(bfs(0, 0))
