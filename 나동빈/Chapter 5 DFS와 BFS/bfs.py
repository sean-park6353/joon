from collections import deque


n = int(input())
graph = [[0]*n for i in range(n)]
visit = [False for i in range(n)]
for i in range(9):
    data = list(map(int, input().split(' ')))
    graph[data[0]-1][data[1]-1] = 1
    graph[data[1]-1][data[0]-1] = 1


def bfs(number):
    visit[number] = True
    q = deque([number])
    while q:
        v = q.popleft()
        print(v+1, end=' ')
        for i in range(len(graph[v])):
            if visit[i] == False and graph[v][i] == 1:
                q.append(i)
                visit[i] = True


for i in graph:
    print(i)
bfs(2)
