a = int(input())
for i in range(a):
    if i == a-1:
        break
    print(' '*i+'*'*(2*a-1-2*i))


for i in range(a):
    print(' '*(a-i-1)+'*'*(i+1)+'*'*(i))
