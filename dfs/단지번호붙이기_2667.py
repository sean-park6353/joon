"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
# n = int(input())

# arr = [] 
# for i in range(n):
#     arr.append(list(map(int, input())))

# print(arr)
n = 7
arr = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], 
[0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]
x_pos = [-1, 1, 0, 0]
y_pos = [0, 0, -1, 1]

table = [[0]*n for _ in range(n)]
area = {}
cnt = 0
def dfs(x, y):
    if arr[x][y] == 1:
        table[x][y] = 1
        origin_x = x
        origin_y = y
        for i in range(4):
            x = origin_x + x_pos[i]
            y = origin_y + y_pos[i]
            if x < 0 or y < 0 or x >= n or y >= n:
                continue
            if table[x][y] == 1:
                continue
            
            if arr[x][y] == 1:
                table[x][y] = 1
                dfs(x, y)
        
    
result = []
for i in range(n):
    for j in range(n):
        x = dfs(i, j)
        print(1)