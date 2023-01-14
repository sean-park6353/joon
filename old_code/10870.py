

arr = [0, 1]
for i in range(22):
    arr.append(arr[i]+arr[i+1])
print(arr[int(input())])
