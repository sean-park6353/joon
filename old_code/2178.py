from collections import deque

xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]
a, b = map(int, input().split(" "))
graph = []
visit = [[0]*b for i in range(a)]
for i in range(a):
    graph.append(list(map(int, input().strip(" "))))


def bfs(m, n):
    visit[0][0] = 1
    q = deque([(m, n)])
    while q:
        if m == a-1 and n == b-1:
            break
        x, y = q.popleft()
        for i in range(4):
            new_x = x+xpos[i]
            new_y = y+ypos[i]
            if new_x >= a or new_y >= b or new_x < 0 or new_y < 0:
                continue
            if visit[new_x][new_y] != 0:
                continue
            if graph[new_x][new_y] != 1:
                continue
            q.append((new_x, new_y))
            visit[new_x][new_y] = visit[x][y]+1
    print(visit[a-1][b-1])


bfs(0, 0)
