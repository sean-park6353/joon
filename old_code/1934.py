def f(a,b):
    if b==0:
        return a
    return f(b,a%b)
for i in range(int(input())):
    a,b=map(int,input().split(" "))
    print(int(a*b/f(a,b)))


