t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dsf(i, j):
    visit[i][j] = True
    for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]
        if ni < 0 or nj < 0 or ni >= b or nj >= a:
            continue
        if visit[ni][nj] == True:
            continue
        if arr[ni][nj] != 1:
            continue
        dsf(ni, nj)


for case in range(t):
    cnt = 0
    a, b, k = map(int, input().split())
    visit = [[False]*a for _ in range(b)]
    # a x b 행렬
    arr = [[0]*a for _ in range(b)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    for i in range(b):
        for j in range(a):
            if arr[i][j] == 1 and visit[i][j] == False:
                dsf(i, j)
                cnt += 1
    print(cnt)
