from collections import Counter
arr = []
for i in range(8):
    arr.append(int(input()))
tmp = dict(zip(arr, range(1, 9)))
a = sorted(arr, reverse=True)[0:5]
answer = []
for i in range(5):
    answer.append(tmp[a[i]])
print(sum(a))
print(*sorted(answer), end=' ')
