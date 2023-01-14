n = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
cnt = []
for i in alpha:
    cnt.append(n.count(i))

for i in range(len(cnt)):
    print(cnt[i], end=' ')
