from collections import deque

xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]
a, b = map(int, input().split(' '))
graph = []
visit = [[0]*b for i in range(a)]
for i in range(a):
    graph.append(list(map(int, input().strip(' '))))
visit[0][0] = 1


def bfs(x, y):
    q = deque([(x, y)])
    while q:
        pop_x, pop_y = q.popleft()
        for i in range(4):
            new_x = pop_x+xpos[i]
            new_y = pop_y+ypos[i]
            if new_x >= a or new_y >= b or new_x < 0 or new_y < 0:
                continue
            if visit[new_x][new_y] != 0:
                continue
            if graph[new_x][new_y] != 1:
                continue
            q.append((new_x, new_y))
            visit[new_x][new_y] = visit[pop_x][pop_y]+1
    print(visit[a-1][b-1])


bfs(0, 0)
