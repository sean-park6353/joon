arr = [1, 1, 2, 2, 2, 8]
user = list(map(int, input().split(' ')))
answer = []
for i in range(6):
    answer.append(arr[i]-user[i])

print(*answer,end=' ')
