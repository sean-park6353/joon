# m, n = list(map(int, ((input().split()))))

m = int(input())
n = int(input())
arr = []

z = 0
if m < n:
    z = m
else:
    z = n

for i in range(z, abs(m-n)+z+1):
    arr.append(i)
res = []
# val = 0
if m == n:
    arr.append(m)
# print(arr)
for i in range(len(arr)):
    cnt = 0
    for j in range(arr[i]):
        if arr[i] % (j+1) == 0:
            cnt = cnt+1
        if cnt >= 3:
            break
    if cnt == 2:
        res.append(arr[i])

# print(res)

if not res:
    print(-1)
else:
    print(sum(res))
    print(min(res))
