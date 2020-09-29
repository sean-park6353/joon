N,M,K=map(int,input().split())
arr=list(map(int,input().split()))
a=max(arr)
arr.pop()
b=max(arr)
arr.append(a)
arr2=[]
cnt=1
sum=0
for i in range(M):
    if (K-1)*cnt+1==K+1:
        sum+=b
        cnt+=1
    sum+=a
    cnt+=1
print(sum)