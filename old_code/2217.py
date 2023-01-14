
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
result = []
for i in range(len(arr)):
    result.append(int(arr[i]*(n-i)))

print(max(result))
