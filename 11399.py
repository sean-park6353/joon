# n = int(input())
# arr = list(map(int, input().split()))
# s = 0
# result = []
# arr.sort()
# for i in arr:
#     s = s+i
#     result.append(s)
# print(sum(result))


a = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()
result = 0
for i in range(len(arr)):
    result = result+arr[i]*(a-i)

print(result)
