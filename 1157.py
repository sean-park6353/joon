

s = input()

s = s.lower()


cnt = []
for i in range(len(s)):
    cnt.append(s.count(s[i]))

print(cnt)
