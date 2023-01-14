N,M=list(map(int,(input().split(' '))))
tmp=list(map(int,(input().split(' '))))


num=[]
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            num.append(tmp[i]+tmp[j]+tmp[k])

d=3000000
result=0
m=[]
for i in range(len(num)):
    if d>abs(M-num[i]):
        d=abs(M-num[i])


for i in range(len(num)):
    if num[i]<=M:
        m.append(num[i])

print(max(m))
