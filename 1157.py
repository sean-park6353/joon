s = input().lower()


if len(s) == 1:
    print(s[0].upper())
else:

    cnt = []
    r = []
    b = []

    for i in range(len(s)):
        b.append(s.index(s[i]))

    b = list(set(b))
    b.sort()
    print(b)

    for i in range(len(b)):
        cnt.append(s.count(s[b[i]]))
        r.append(s.count(s[b[i]]))

# print(cnt)

    tmp = max(cnt)
    cnt.remove(tmp)
    tmp2 = max(cnt)

    if tmp == tmp2:
        print("?")
    else:
        for i in range(len(s)):
            if max(r) == s.count(s[i]):
                print(s[i].upper())
                break
