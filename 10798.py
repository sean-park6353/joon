arr=[]
big=0
for i in range(5):
    insert=list(map(str,input().strip(" ")))
    if len(insert)>=big:
        big=len(insert)
        arr.append(insert)
    else:
        w=big-len(insert)
        for j in range(w):
            insert.append(" ")
        arr.append(insert)
for i in range(5):
    if len(arr[i])!=big:
        w=big-len(arr[i])
        for j in range(w):
            arr[i].append(" ")

answer=[]
for i in range(big):
    for j in range(5):
        if arr[j][i]!=" ":
            answer.append(arr[j][i])
for i in answer:
    print(i,end='')

