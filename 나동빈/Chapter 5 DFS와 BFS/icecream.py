n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

cnt = 0


def dsf(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        dsf(x-1, y)
        dsf(x, y-1)
        dsf(x, y+1)
        dsf(x+1, y)
        return True
    return False


for i in range(len(arr)):
    for j in range(len(arr[i])):
        if dsf(i, j) == True:
            cnt += 1

print(cnt)
