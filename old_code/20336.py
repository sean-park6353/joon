import random
from itertools import combinations
menu = []
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(str, input().split(' '))))
for i in arr:
    menu.append((i[1:]))
merge_menu = []
for i in menu:
    merge_menu.extend(i)
menu.clear()
merge_menu = list(set(merge_menu))
cnt = random.randint(1, len(merge_menu))
print(cnt)
ind = []
flg = 0
for i in range(cnt):
    if flg == 0:
        tmp = random.randint(0, len(merge_menu)-1)
        ind.append(tmp)
        flg += 1
        continue
    while True:
        tmp = random.randint(0, len(merge_menu)-1)
        if tmp not in ind:
            ind.append(tmp)
            break
answer = list(combinations(merge_menu, len(ind)))[random.randint(
    0, len(list(combinations(merge_menu, len(ind))))-1)]
for i in answer:
    print(i)
