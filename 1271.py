a = input()
arr = []
for i in a:
    if i.isalpha() == True:
        arr.append(i)
    else:
        arr.append(int(i))
d = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

arr = [d[item] for item in arr]
arr = arr[::-1]

tmp = []
for i in range(len(arr)):
    tmp.append(arr[i]*(16**(i)))

print(sum(tmp))
