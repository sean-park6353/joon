k = int(input())
n = 0
tmp = int(k/3)
while n*n+n <= tmp:
    n = n+1
n = n-1


while k <= 3*(n+1)*(n+2) and 3*n*(n+1)+1 < k:
    n = n+1

if k > 1:
    print(n+1)
elif k == 1:
    print(1)
else:
    print(n+1)

# while k > 3*(n+1)*(n+2):
#     n = n+1

# print(n+1)
