n, m, v = map(int, input().split())
result = [False]*n
arr = []
for i in range(m):
    arr.append(list(map(int, input().split())))


def dfs(arr, v, result):
    print(v, end=' ')
    result[v-1] = True
    for i in range(len(arr)):
        if v in arr[i]:
            result[v] = True


dfs(arr, v, result)
