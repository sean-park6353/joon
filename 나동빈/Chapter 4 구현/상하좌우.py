# import numpy as np
# n = int(input())
# arr = input().split()
# s = np.array([1, 1])


# for i in range(len(arr)):
#     if arr[i] == 'R':
#         s = s+np.array([0, 1])
#         if s[0] > n or s[1] > n or s[0] <= 0 or s[1] <= 0:
#             s = s-np.array([0, 1])
#     elif arr[i] == 'L':
#         s = s-np.array([0, 1])
#         if s[0] > n or s[1] > n or s[0] <= 0 or s[1] <= 0:
#             s = s+np.array([0, 1])
#     elif arr[i] == 'D':
#         s = s+np.array([1, 0])
#         if s[0] > n or s[1] > n or s[0] <= 0 or s[1] <= 0:
#             s = s-np.array([1, 0])
#     elif arr[i] == 'U':
#         s = s-np.array([1, 0])
#         if s[0] > n or s[1] > n or s[0] <= 0 or s[1] <= 0:
#             s = s+np.array([1, 0])


# print(s)


n = int(input())
x, y = 1, 1
plans = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'D', 'U']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

print(x, y)
