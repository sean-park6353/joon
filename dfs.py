cnt = 0


def dfs(num):
    global cnt
    visit[num] = True
    # print(num, end=' ')
    for i in graph[num]:
        if visit[i] == False:  # 방문이 안 됐다면,
            visit[i] = True
            cnt += 1
            dfs(i)
    return cnt


visit = [False for i in range(9)]
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

print(dfs(1))
