

a=int(input())
arr=[]
cnt=[]
for i in range(a):
    arr.append(list(map(int,input().split())))
    cnt.append(1)
index=0
for i in arr:
    for j in arr:
        if i[0]<j[0] and i[1]<j[1]:
            cnt[index]+=1
    index+=1    

for i in cnt:
    print(i,end=' ')
