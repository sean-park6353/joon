n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(str, input())))


sorted(arr, key=lambda x: len(arr))

print(arr)
