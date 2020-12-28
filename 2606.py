# import sys
# sys.setrecursionlimit(50000)


# def dfs(node, n):
#     global cnt
#     visit[node] = True
#     for i in range(1, n+1):
#         if visit[i] == False and arr[node][i] == 1:
#             cnt += 1
#             dfs(i, n)


# cnt = 0
# n = int(input())
# m = int(input())
# visit = [False]*(n+1)
# arr = [[0]*(n+1) for _ in range(n+1)]


# for i in range(m):
#     link = list(map(int, input().split(' ')))
#     arr[link[0]][link[1]] = 1
#     arr[link[1]][link[0]] = 1


# dfs(1, n)
# print(arr)
