n = int(input())
arr = []
for i in range(n):
    arr.append(input())
arr = list(set(arr))
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if len(arr[i]) < len(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
        if len(arr[i]) == len(arr[j]):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
arr.reverse()
for i in arr:
    print(i)
