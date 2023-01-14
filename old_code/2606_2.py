n = int(input())
edge = int(input())
visit = [False for i in range(n)]
graph = [[0]*n for i in range(n)]
for i in range(edge):
    data = list(map(int, input().split(' ')))
    graph[data[0]-1][data[1]-1] = 1
    graph[data[1]-1][data[0]-1] = 1
cnt = 0


def dfs(n):
    global cnt
    cnt += 1
    visit[n] = True
    for i in range(len(graph[n])):
        if graph[n][i] == 1 and visit[i] == False:
            dfs(i)


dfs(0)
print(cnt-1)
