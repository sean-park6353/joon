n = int(input())
arr = list(map(int, input().split(' ')))
cnt = 0
tmp = []
for i in range(len(arr)):
    if arr[i] == 2 or arr[i] == 0:
        tmp.append(arr[i])
    if tmp == [2, 0, 2, 0]:
        cnt += 1
        tmp.clear()


print(cnt)
