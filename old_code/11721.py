n = input()

arr = []
m = ""
i = 0

for j in range(len(n)):
    if i == 10:
        i = 0
        arr.append(m)
        m = ""
    m += n[j]
    i += 1
    if j == len(n)-1 and len(m) <= 10:
        arr.append(m)
for i in range(len(arr)):
    print(arr[i])
