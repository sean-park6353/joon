from itertools import combinations


a = list(map(int, input().split(' ')))
N = a[0]
M = a[1]

card = list(map(int, input().split(' ')))
arr = list(combinations(card, 3))

print(arr)
min_value = sum(max(arr))
min_tuple = max(arr)
print(min_tuple)
tmp_tuple = ()
tmp_value = 1
while min_value > M:
    arr.remove(min_tuple)
    min_value = sum(max(arr))
    min_tuple = max(arr)
    tmp_tuple = min_tuple
    tmp_value = min_value

print(tmp_value)
