
from itertools import combinations
a, b = map(int, input().split(' '))
pw = list(map(str, input().split(' ')))
pw.sort()
answer = list(combinations(pw, a))
alpha = [chr(i) for i in range(97, 123)]
for i in alpha:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        alpha.remove(i)
result = []
for data in answer:
    cnt = 0
    if 'a' in data or 'e' in data or 'i' in data or 'o' in data or 'u' in data:
        for alphabet in alpha:
            if alphabet in data:
                cnt += 1
        if cnt >= 2:
            result.append(data)
for i in result:
    for j in i:
        print(j, end='')
    print()
