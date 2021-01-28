from math import sqrt
a=int(input())
b=int(input())

arr=[]
for i in range(a,b+1):
    if sqrt(i).is_integer():
        arr.append(i)

if len(arr)==0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))

