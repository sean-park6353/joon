a = list(map(int, list(input())))
a.sort(reverse=True)
for i in a:
    print(i, end='')
