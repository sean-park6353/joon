t = int(input())
result = []

for i in range(t):
    arr = []
    n = int(input())
    for j in range(n):
        arr.append(list(map(int, input().split(' '))))
    arr.sort()
    cnt = 1
    min = arr[0][1]
    for j in range(1, n):
        if arr[j][1] < min:
            min = arr[j][1]
            cnt += 1
    print(cnt)
