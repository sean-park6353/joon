
# 에라토스테네스의 체 시간초과

m, n = list(map(int, ((input().split()))))
z = 0
if m < n:
    z = m
else:
    z = n
res = []
arr = []
for i in range(z, abs(m-n)+z+1):
    arr.append(i)


val = []


size = abs(m-n)+z-1
for i in range(size):
    val.append(i+2)
# print(val)
# print(size)
for i in range(len(val)):
    for j in range(i+1, len(val)):
        if res.count(val[j]) == 1:
            continue
        if val[j] % val[i] == 0:
            res.append(val[j])


# print(arr)

res = list(set(res))

for i in range(len(res)):
    arr.remove(res[i])

if arr[0] == 1:
    arr.remove(1)

for i in range(len(arr)):
    print(arr[i], end="\n")
