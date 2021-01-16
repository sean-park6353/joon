a, b = map(int, input().split(" "))
x = []
for i in range(a):
    x.append(list(map(int, input().split(' '))))
c, d = map(int, input().split(" "))
y = []
for i in range(c):
    y.append(list(map(int, input().split(' '))))

for i in x:
    print(i)

for i in y:
    print(i)
