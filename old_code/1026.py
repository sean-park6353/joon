a = int(input())
arr = list(map(int, input().split(' ')))
brr = list(map(int, input().split(' ')))
crr = sorted(brr, reverse=True)
drr = sorted(arr)
index = []
for i in crr:
    index.append(brr.index(i))
for i in range(len(index)):
    tmp = index[i]
    arr[tmp] = drr[i]
c = 0
for i in range(a):
    c += arr[i]*brr[i]
print(c)
