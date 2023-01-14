n = int(input())
arr = input().split()
arr = list(map(int, arr))
val = 0

for i in range(len(arr)):
    cnt = 0
    for j in range(arr[i]):
        if arr[i] % (j+1) == 0:
            cnt = cnt+1
    if cnt == 2:
        val = val+1


print(val)
