n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(str, input().split())))

print(arr[0:8][0:8])

for i in range(len(arr)):
    print(arr[i:8+i][i:8+i])
