a, b = map(int, input().split(" "))
tree = list(map(int, input().split(" ")))
tree.sort(reverse=True)
h = max(tree)
meter = 0
while meter != b:
    meter = 0
    for i in tree:
        if h < i:
            meter += i-h
    h -= 1
print(h-1)
