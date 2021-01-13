a, b = map(int, input().split(' '))
tree = list(map(int, input().split(' ')))
l, r = 1, max(tree)

while l <= r:
    m = (l+r)//2
    tmp = 0
    for i in tree:
        if i >= m:
            tmp += i-m

    if tmp >= b:  # 더 깎아야 한다
        l = m+1
    else:  # 그만 깎아야 한다
        r = m-1

print(end)
