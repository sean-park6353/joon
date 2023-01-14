x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

arrx = []
arry = []
arrx.append(x1)
arrx.append(x2)
arrx.append(x3)
arry.append(y1)
arry.append(y2)
arry.append(y3)

x4 = 0
y4 = 0
for i in range(len(arrx)):
    if arrx.count(arrx[i]) == 1:
        x4 = arrx[i]
for i in range(len(arry)):
    if arry.count(arry[i]) == 1:
        y4 = arry[i]

print(x4, y4)
