# cnt = 0
# a = int(input())
# b = int(input())
# g = [[]]
# result = []
# for i in range(1, b+1):
#     tmp = list(map(int, input().split(' ')))
#     g.append(tmp)


def dfs(num):
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
