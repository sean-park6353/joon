import sys
n = int(input())
arr = [0]*10001
for i in range(n):
    arr[int(sys.stdin.readline())] += 1

arr.sort()
# for i in range(n):
#     sys.stdout.write(str(arr[i]))
#     sys.stdout.write('\n')

print(arr)
