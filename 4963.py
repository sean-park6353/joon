cnt = 0
visit = []
arr = []
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]


def dfs(i, j, a, b):
    visit[i][j] = True
    for k in range(8):
        ni = i+dx[k]
        nj = j+dy[k]
        if ni < 0 or nj < 0 or ni >= b or nj >= a:
            continue
        if visit[ni][nj] == True:
            continue
        if arr[ni][nj] != 1:
            continue
        dfs(ni, nj, a, b)


while True:
    land = 0
    a, b = map(int, input().split(' '))
    if a == 0 and b == 0:
        break
    visit = [[False]*a for _ in range(b)]
    # print(visit)
    # visit[0][1] = True
    # print(visit)
    arr = []
    for i in range(b):
        arr.append(list(map(int, input().split(' '))))
    for i in range(b):
        for j in range(a):
            if arr[i][j] == 1:
                land += 1
                dfs(i, j, a, b)

    # visit[0][1] = True
    print(land)
