n = int(input())
arr = [300, 60, 10]
cnt = []
for i in range(3):
    c = int(n/arr[i])
    n = n-c*arr[i]
    cnt.append(c)


if n != 0:
    print(-1)
else:
    for i in cnt:
        print(i, end=' ')
