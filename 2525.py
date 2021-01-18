t, m = map(int, input().split(' '))
a = int(input())
m += a
b = a//60
if m >= 60:
    t += 1
    m -= 60*b

print(t, m)
