n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
answer = max(arr)
z = []
while True:
    tmp = []
    for i in range(n):
        tmp.append(arr[i] % answer)
    if len(set(tmp)) == 1:
        z.append(answer)
    if answer == 2:
        break
    answer -= 1
z.sort()
print(*z, end=' ')
