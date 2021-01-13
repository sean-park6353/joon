a = int(input())
arr = []
for i in range(a):
    data = input().split(' ')
    arr.append((data[0], int(data[1])))


print(*sorted(arr, key=lambda x: x[1]), sep='\n')
