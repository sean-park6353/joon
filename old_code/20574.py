graph = [[0]*8 for _ in range(8)]

a, b = map(int, input().split(' '))
pos = input()
y = ord(pos[0])-97
x = 0
tmp = 0
while True:
    if tmp == 7:
        break
    tmp = int(pos[1])+x
    x += 1

# print(x, y)


def func(x, y, a, b):
    xpos = []
    for i in range(8):
        new_x = x+b
        new_y = y+a
        if new_x < 0 or new_y < 0 or new_x >= 8 or new_y >= 8:
            continue
        graph[new_x][new_y] = 1
    # for i in graph:
    #     print(i)


print(x, y)
func(x, y, a, b)
