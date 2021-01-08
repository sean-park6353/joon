from collections import deque
import copy

xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]
a, b = map(int, input().split(' '))
graph = []
for i in range(b):
    graph.append(list(map(int, input().split(" "))))
visit = copy.deepcopy(graph)

q = deque([])

minus_arr = []
for i in range(b):
    for j in range(a):
        if graph[i][j] == 1:
            q.append((i, j))
        elif graph[i][j] == -1:
            minus_arr.append((i, j))

while q:
    x, y = q.popleft()
    for i in range(4):
        new_x = x+xpos[i]
        new_y = y+ypos[i]
        if new_x >= b or new_y >= a or new_x < 0 or new_y < 0:
            continue
        if graph[new_x][new_y] != 0:
            continue
        if visit[new_x][new_y] != 0:
            continue
        visit[new_x][new_y] = visit[x][y]+1
        graph[new_x][new_y] = 1
        q.append((new_x, new_y))

flg = False
for i in range(len(visit)):
    if 0 in visit[i]:
        flg = True

result = []
for i in range(len(visit)):
    result.append(max(visit[i]))
if flg == True:
    print(-1)
else:
    print(max(result)-1)
