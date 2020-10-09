arr = []
i = 0


def power(n):
    return n**2


while True:
    arr.append(list(map(int, input().split())))
    if sum(arr[i]) == 0:
        arr.pop()
        break
    i += 1

result = []
# print(arr)
for i in arr:
    i = list(map(power, i))
    if i[0]+i[1] == i[2] or i[0]+i[2] == i[1] or i[1]+i[2] == i[0]:
        result.append('right')
    else:
        result.append('wrong')

for i in result:
    print(i)
