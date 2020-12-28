
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())
brr = list(map(int, sys.stdin.readline().split()))



# tmp = set(arr)-(set(arr)-(set(brr)))
# value = list(tmp)
# result = [0 for i in range(k)]
# z = []
# for i in range(len(value)):
#     z.append(brr.index(value[i]))
# for i in range(len(z)):
#     result[z[i]] += 1
# print(*result, sep=' ')
284,000