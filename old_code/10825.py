a = int(input())
arr = []
for i in range(a):
    tmp = tuple(map(str, input().split(' ')))
    new_tuple = tuple((tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])))
    arr.append(new_tuple)
x = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for a, b, c, d in x:
    print(a)
