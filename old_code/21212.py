n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
flg=False
cnt=0
answer=[]
for ingredient,needs in arr:
    if ingredient> needs:
        print(0)
        flg=True
        break
    cakes=needs//ingredient
    answer.append(cakes)
if flg==False:
    print(min(answer))
