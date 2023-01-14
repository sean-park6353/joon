from collections import Counter
a=input().lower()
arr=list(map(str,a.strip('')))
answer=Counter(arr)

big=0
tmp=""
for i,j in answer.items():
    if big<j:
        big=j
        tmp=i
cnt=0
result=[]
for i,j in answer.items():
    if j==big:
        cnt+=1
    if cnt>=2:
        result.append('?')
        break
if cnt>=2:
    print(result[0])
else:
    print(tmp.upper())