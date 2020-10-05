n = int(input())
arr = list(map(int, input().split()))
s = 0
result = []
arr.sort()
for i in arr:
    s = s+i
    result.append(s)
print(sum(result))
