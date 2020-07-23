

def is_han(a):
    tmp = []
    a = str(a)
    if a == 0:
        return 0

    if len(a) == 1:
        return 1
    for i in range(len(a)):
        tmp.append(a[i])
    differ = int(tmp[0])-int(tmp[1])
    for i in range(len(tmp)-1):
        if int(tmp[i])-int(tmp[i+1]) != differ:
            return 0

    return 1


a = int(input())


cnt = 0
for i in range(1, a+1):
    if is_han(i) == 1:
        cnt = cnt+1
print(cnt)
