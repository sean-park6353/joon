
m, n = list(map(int, input().split()))

arr = []
k = 0
for i in range(1000001):
    arr.append(0)
arr[1] = 1

for i in range(2, 1000001):
    if arr[i] == 0:
        for j in range(i+i, 1000001, i):
            k = j
            arr[j] = 1

cnt = 0
for i in range(m, n+1):
    if arr[i] == 0:
        print(i)
        cnt = cnt+1


print(cnt)
