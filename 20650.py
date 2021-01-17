import copy
arr = list(map(int, input().split(' ')))
arr.sort()
brr = copy.deepcopy(arr)
a = min(arr)
b = 0
c = 0
a_b_c = max(arr)
b_c = a_b_c-a
arr.remove(a)
arr.remove(a_b_c)
arr.remove(b_c)
flg = False
for i in range(4):
    for j in range(4):
        if i != j:
            if arr[i]+arr[j] == b_c:
                b = arr[i]
                c = arr[j]
                flg = True
                break
    if flg == True:
        break
print(a, b, c)
