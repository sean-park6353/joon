n, m, v = map(int, input().split())
arr = []
for i in range(m):
    arr.append(list(map(int, input().split())))

result = [False]*n
def dfs(arr, v):
    print(v, end=' ')
    for i in range(len(arr)):
        if v in arr[i]:
            tmp = arr[i]
            break
