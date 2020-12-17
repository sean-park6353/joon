a, b = map(int, input().split(' '))
arr = []
for i in range(a):
    arr.append(list(map(int, input().split(' '))))

small = []
for i in arr:
    small.append(min(i))

print(max(small))
