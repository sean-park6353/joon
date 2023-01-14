from operator import itemgetter
n = int(input())

arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split(' '))))
arr.sort(key=itemgetter(1, 0))


flg = arr[0]
result = [flg]
for i in range(1, len(arr)):
    if flg[1] <= arr[i][0]:
        flg = arr[i]
        result.append(arr[i])


print(len(result))
