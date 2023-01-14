# 먼저 입력을 이렇게 받는다.


# 이제 코드를 합쳐 보자
xpos = [-1, 1, 0, 0, -1, -1, 1, 1]
ypos = [0, 0, -1, 1, -1, 1, -1, 1]

result = []


def dfs(x, y):
    visit[x][y] = True
    for i in range(8):
        new_x = x+xpos[i]
        new_y = y+ypos[i]
        if new_x < 0 or new_y < 0 or new_x >= b or new_y >= a:  # 값을 넘어가는 경우
            continue
        if visit[new_x][new_y] == True:  # 이미 방문을 한 경우
            continue
        if graph[new_x][new_y] != 1:  # 연결이 되어있지 않은 경우
            continue
        dfs(new_x, new_y)


while(True):
    graph = []
    a, b = map(int, input().split(' '))
    visit = [[False]*a for i in range(b)]
    if a == 0 and b == 0:
        break
    for i in range(b):
        graph.append(list(map(int, input().split(' '))))
    cnt = 0
    for i in range(b):
        for j in range(a):
            if graph[i][j] == 1 and visit[i][j] == False:
                dfs(i, j)
                cnt += 1
    print(cnt)

# cnt = 0
# visit = []
# arr = []
# dx = [-1, 1, 0, 0, -1, -1, 1, 1]
# dy = [0, 0, -1, 1, -1, 1, 1, -1]


# def dfs(i, j, a, b):
#     visit[i][j] = True
#     for k in range(8):
#         ni = i+dx[k]
#         nj = j+dy[k]
#         if ni < 0 or nj < 0 or ni >= b or nj >= a:
#             continue
#         if visit[ni][nj] == True:
#             continue
#         if arr[ni][nj] != 1:
#             continue
#         dfs(ni, nj, a, b)


# while True:
#     land = 0
#     a, b = map(int, input().split(' '))
#     if a == 0 and b == 0:
#         break
#     visit = [[False]*a for _ in range(b)]
#     # print(visit)
#     # visit[0][1] = True
#     # print(visit)
#     arr = []
#     for i in range(b):
#         arr.append(list(map(int, input().split(' '))))
#     for i in range(b):
#         for j in range(a):
#             if arr[i][j] == 1:
#                 land += 1
#                 dfs(i, j, a, b)

#     # visit[0][1] = True
#     print(land)
