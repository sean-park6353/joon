from collections import deque
a, b, v = map(int, input().split(" "))
graph = [[0]*a for i in range(a)]
visit = [False for i in range(a)]
for i in range(b):
    data = list(map(int, input().split(' ')))
    graph[data[0]-1][data[1]-1] = 1
    graph[data[1]-1][data[0]-1] = 1


def dfs(n):
    visit[n] = True
    print(n+1, end=' ')
    for i in range(len(graph[n])):
        if graph[n][i] == 1 and visit[i] == False:
            dfs(i)


def bfs(n):
    visit[n] = True
    q = deque([n])
    while q:
        tmp = q.popleft()
        print(tmp+1, end=' ')
        for i in range(len(graph[tmp])):
            if visit[i] == False and graph[tmp][i] == 1:
                visit[i] = True
                q.append(i)


dfs(v-1)
visit = [False for i in range(a)]
print()

bfs(v-1)
