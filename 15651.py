N,M=map(int,input().split())

from itertools import product
a=[]
item=[]

for i in range(N):
    item.append(i+1)


for i in list(product(item,repeat=M)):
    a.append(list(map(int,i)))

for i in a:
    print(' '.join(map(str,i)))
