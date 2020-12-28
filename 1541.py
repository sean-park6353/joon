arr = input().split('-')
result = 0
for i in arr[0].split('+'):
    result += int(i)  # 첫 번째 값 더하기 성공
for i in arr[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)
