n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dsf(x, y):
    print(2)


result = 0
for i in range(n):
    for j in range(m):
        if dsf(i, j) == True:
            result += 1

print(result)
