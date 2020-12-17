n, w = map(int, input().split())
arr = []
big = 0
index = 0
for i in range(n):
    arr.append(int(input()))
    if w - arr[i] >= 0:
        big = arr[i]
        index = i
cnt = 0
m = 0
while True:
    if w/big >= 1:
        m += int(w/big)
    w = w % big
    big = arr[index-1]
    index -= 1
    cnt += 1
    if w == 0:
        break

print(m)


n, k = map(int, input().split(' '))

arr = []
for i in range(n):
    arr.append(int(input()))

arr = arr[::-1]
x = 0
result = []
for i in range(len(arr)):
    cnt = int(k/arr[i])
    if cnt != 0:
        k = k-cnt*arr[i]
        result.append(cnt)

print(sum(result))
