def dfs(graph, v, arr):
    arr[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not arr[i]:
            dfs(graph, i, arr)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

arr = [False]*9

dfs(graph, 1, arr)
