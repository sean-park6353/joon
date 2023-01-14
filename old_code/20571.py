name, floor = map(str, input().split(' '))
floor = int(floor)
if name == 'residential':
    if floor == 1:
        print(0)
    elif 2 <= floor <= 5:
        print(1)
    elif 6 <= floor <= 10:
        print(2)
    elif 11 <= floor <= 15:
        print(3)
    else:
        print(4)
elif name == "commercial":
    if floor == 1:
        print(0)
    elif 2 <= floor <= 7:
        print(1)
    elif 8 <= floor <= 14:
        print(2)
    else:
        print(3)
else:
    if floor == 1:
        print(0)
    elif 2 <= floor <= 4:
        print(1)
    elif 5 <= floor <= 8:
        print(2)
    elif 9 <= floor <= 12:
        print(3)
    elif 13 <= floor <= 16:
        print(4)
    else:
        print(5)
