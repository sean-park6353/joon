import sys
sys.setrecursionlimit(50000)
c = int(input())
n = int(input())
cnt = 0
arr = [[0]*(c+1) for _ in range(c+1)]
visit = [False]*(c+1)
for i in range(n):
    link = list(map(int, input().split(' ')))
    arr[link[0]][link[1]] = 1
    arr[link[1]][link[0]] = 1


def dfs(k, c):
    global cnt
    visit[k] = True
    for i in range(1, c+1):
        if arr[k][i] == 1 and visit[i] == False:
            cnt += 1
            dfs(i, c)


dfs(1, c)
result = [i for i in visit if i == True]
# print(arr)
# print(len(result)-1)
print(len(result)-1)
