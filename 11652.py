from collections import Counter
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

brr = Counter(arr)
answer = sorted(brr.items(), key=lambda x: (-x[1], x[0]))
print(answer[0][0])
