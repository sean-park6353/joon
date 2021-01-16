a = list(map(str, input().strip(" ")))
b = list(map(str, input().strip(" ")))
cnt = 0
for i in a:
    if i in b:
        cnt += 1
print(a, b)
