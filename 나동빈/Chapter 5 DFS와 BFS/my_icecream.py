n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dsf(x, y):
    if x >= n or y >= n or x <= -1 or y <= -1:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dsf(x+1, y)
        dsf(x, y+1)
        dsf(x, y-1)
        dsf(x-1, y)
        return True
    return False


cnt = 0

for i in range(n):
    for j in range(m):
        if dsf(i, j) == True:
            cnt += 1

print(cnt)
