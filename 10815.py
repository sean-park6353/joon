n = int(input())
arr = list(map(int, input().split(' ')))
k = int(input())
result = list(map(int, input().split(' ')))
arr.sort()
left = arr.index(arr[0])  # 0
right = arr.index(arr[-1])  # 5
middle = int((left+right)/2)
brr = [0 for i in range(k)]
for i in range(k):   # result : 1,3,7,9,5
    left = arr.index(arr[0])  # 0
    right = arr.index(arr[-1])  # 5
    middle = int((left+right)/2)
    if result[i] == arr[right]:
        brr[i] += 1
        continue
    while left <= right:
        middle = int((left+right)/2)
        if result[i] < arr[middle]:
            right = middle-1
        elif result[i] > arr[middle]:
            left = middle+1
        else:
            brr[i] += 1
            break
for i in brr:
    print(i, end=' ')
