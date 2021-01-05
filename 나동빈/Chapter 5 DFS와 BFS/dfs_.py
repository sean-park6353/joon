n = int(input())
graph = [[0]*n for i in range(n)]
visit = [False for i in range(n)]
for i in range(9):
    data = list(map(int, input().split(' ')))
    graph[data[0]-1][data[1]-1] = 1
    graph[data[1]-1][data[0]-1] = 1


def dfs(number):
    visit[number] = True
    print(number+1, end=' ')
    for i in range(len(graph[number])):
        if graph[number][i] == 1 and visit[i] == False:
            dfs(i)


print(graph)
dfs(0)
