from sys import stdin
from sys import stdout
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(str, stdin.readline().split(' '))))

for i in range(n):
    arr[i][0] = int(arr[i][0])
    arr[i].append(i)
# print(arr)
new_list = sorted(arr, key=lambda x: (x[0], x[2]))

for i in range(len(arr)):
    stdout.write(str(new_list[i][0]))
    stdout.write(' ')
    stdout.write(new_list[i][1])
