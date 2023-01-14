n,m,k=map(int,input().split())
arr=list(map(int,input().split()))

a=max(arr)
arr.pop()
b=max(arr)
arr.append(a)

cnt=0
sum=0


for i in range(m):
    if cnt==k:
        cnt=0
        sum+=b
    else:
        sum+=a
        cnt+=1

print(sum)