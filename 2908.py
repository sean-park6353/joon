
def reverse(arr):
    arr[0][0], arr[0][2] = arr[0][2], arr[0][0]
    return arr


arr = list(map(str, input().split()))
print(arr)
# result = list(map(reverse, arr))
# print(result)
