n = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
cnt = []
for i in alpha:
    cnt.append(n.count(i))
print(cnt)
