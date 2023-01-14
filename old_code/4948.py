
# 베르트랑 공준
m = []

tmp = 1
while tmp != 0:
    tmp = int(input())
    m.append(tmp)

m.remove(0)

cnt = []
for i in range(len(m)):
    cnt.append(0)
arr = []
k = 0
for i in range(300000):
    arr.append(0)
arr[1] = 1

for i in range(2, 300000):
    if arr[i] == 0:
        for j in range(i+i, 300000, i):
            k = j
            arr[j] = 1

for i in range(len(m)):
    for j in range(m[i]+1, 2*m[i]+1):
        if arr[j] == 0:
            cnt[i] = cnt[i]+1

for i in range(len(m)):
    print(cnt[i])
