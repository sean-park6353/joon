

def dfs(p):
    visit[p] = True
    for i in range(len(graph[p])):
        if visit[i] == False and graph[p][i] == 1:
            visit[i] = True
            dfs(i)


a, b = map(int, input().split(' '))
graph = [[0]*a for p in range(a)]
visit = [False for p in range(a)]


for j in range(b):
    data = list(map(int, input().split(' ')))
    graph[data[1]-1][data[0]-1] = 1
    graph[data[0]-1][data[1]-1] = 1
result = []
cnt = 0
for i in range(a):
    if visit[i] != True:
        dfs(i)
        cnt += 1
print(cnt)
