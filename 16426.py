import copy
a, b = map(int, input().split(" "))
graph = []
xpos = [-1, 1, 0, 0]
ypos = [0, 0, -1, 1]
for i in range(a):
    graph.append(list(map(int, input().split(" "))))
result = copy.deepcopy(graph)
for i in range(a):
    for j in range(b):
        cnt = 0
        for k in range(4):
            new_x = i+xpos[k]
            new_y = j+ypos[k]
            if new_x < 0 or new_y < 0 or new_x >= a or new_y >= b:
                continue
            if graph[i][j] < graph[new_x][new_y]:
                cnt += 1
        if cnt == 4:
            result[i][j] = 1
        else:
            result[i][j] = 0
for i in range(a):
    for j in range(b):
        print(result[i][j], end=' ')
    print()
