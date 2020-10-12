n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)


def dsf(x, y, p):
    if x >= n or y >= n or x <= -1 or y <= -1:
        return 0
    if graph[x][y] == 1:
        graph[x][y] = 0
        p += 1
        tmp1 = dsf(x+1, y, p)
        tmp2 = dsf(x, y+1, tmp1)
        tmp3 = dsf(x-1, y, tmp2)
        tmp4 = dsf(x, y-1, tmp3)
        return tmp4
    return 0


cnt = 0
result = []
for i in range(n):
    for j in range(n):
        if dsf(i, j, 0) != 0:
            cnt += 1

print(cnt)


