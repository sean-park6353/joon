from bisect import bisect_left, bisect_right

from collections import Counter
p.sort()
c.sort()

a = Counter(p)
b = Counter(c)

for i, j in a.items():
    try:
        if a[i] != b[i]:
            print(i)
    except:
        print(i)
