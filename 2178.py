from collections import deque
a, b = map(int, input().split(' '))
graph = []
xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]
visit = [[0]*b for i in range(a)]
for i in range(a):
    graph.append(list(map(int, input().strip())))
q = deque([(0, 0)])
visit[0][0] = 1
while q:
    (x, y) = q.popleft()
    if x == a-1 and y == b-1:  # 최종 경로 도착
        print(visit[x][y])
        break
    for i in range(4):
        new_x = x+xpos[i]
        new_y = y+ypos[i]
        if new_x >= a or new_y >= b or new_x < 0 or new_y < 0:
            continue
        if visit[new_x][new_y] == True:
            continue
        if graph[new_x][new_y] != 1:
            continue
        visit[new_x][new_y] = True
        visit[new_x][new_y] = visit[x][y]+1
        q.append((new_x, new_y))
