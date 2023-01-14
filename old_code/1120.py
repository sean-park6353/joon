from collections import Counter
x,y=map(str,input().split())

print(Counter(x))
print(Counter(y))

a=Counter(y)-Counter(x)
print(a)