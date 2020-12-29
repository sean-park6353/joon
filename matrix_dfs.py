
cnt = 0


def dfs(num):
    global cnt
    visit[num] = True
    for i in range(len(graph[num])):
        if visit[i] == False and graph[num][i] == 1:
            cnt += 1
            dfs(i)
    return cnt


a = int(input())
b = int(input())

graph = [[0]*a for i in range(a)]

for i in range(b):
    data = list(map(int, input().split(' ')))
    graph[data[0]-1][data[1]-1] = 1
    graph[data[1]-1][data[0]-1] = 1
visit = [False for i in range(7)]

# graph = [
#     [0, 1, 0, 0, 1, 0, 0],  # 1
#     [1, 0, 1, 0, 1, 0, 0],  # 2
#     [0, 1, 0, 0, 0, 0, 0],  # 3
#     [0, 0, 0, 0, 0, 0, 1],  # 4
#     [1, 1, 0, 0, 0, 1, 0],  # 5
#     [0, 0, 0, 0, 1, 0, 0],  # 6
#     [0, 0, 0, 1, 0, 0, 0]   # 7
# ]

print(dfs(0))
