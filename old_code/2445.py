a = int(input())


for i in range(a):
    print('*'*(i+1)+' '*((-2*(i+1))+(2*a))+'*'*(i+1))
for i in range(a):
    if i == (a-1):
        break
    print('*'*(a-i-1)+' '*((2*i)+2)+'*'*(a-i-1))
