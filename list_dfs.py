def dfs(num):
    global
    visit[num] = True
    print(num, end=' ')
    for i in graph[num]:
        if visit[i] == False:  # 방문하지 않았다면
            dfs(i)


visit = [False for i in range(8)]
graph = [

    [],  # 0
    [2, 5],  # 1
    [3, 5],  # 2
    [2],
    [7],
    [1, 2, 6],
    [5],
    [4]

]

dfs(1)
