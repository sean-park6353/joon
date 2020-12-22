from itertools import combinations

arr = []
for i in range(9):
    arr.append(int(input()))


brr = list(combinations(arr, 7))

result = []
for i in brr:
    if sum(i) == 100:
        result.append(i)
result = sorted(result[0])


for i in result:
    print(i)
