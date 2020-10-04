import math
n=int(input())

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

tmp=[]
tmp.append(math.factorial(sum(arr2)))
for i in range(len(arr2)):
    tmp.append(math.factorial(arr2[i]))

val=1

for i in range(1,len(tmp)):
    val*=tmp[i]
val=int(tmp[0]/val)
# print(tmp)
print(val)

result=[]
for i in range(val):
    result.append(arr)

# for i in range(val):
    



# N,M=map(int,input().split())



# for i in list(combinations([1,2,3,4],/)):
#     a.append(list(map(int,i)))
# print(a)
# for i in range(N):
#     item.append(i+1)


# for i in list(product(item,repeat=M)):
#     a.append(list(map(int,i)))

# for i in a:
#     print(' '.join(map(str,i)))