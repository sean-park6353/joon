num = int(input())
flg = 1
n = 1
while True:
    if num == 1:
        flg = 0
        break
    if n**2+n+2 <= num*2 and num*2 < n**2+3*n+4:
        break
    else:
        n += 1


origin = int(n*(n+1)/2+1)
differ = abs(origin-num)


tmp = '/'

if flg == 0:
    print("{}{}{}".format(1, '/', 1))
else:
    if n % 2 != 0:
        u = 1
        d = n+1
        for i in range(differ):
            u += 1
            d -= 1
        print("{}{}{}".format(u, tmp, d))
    else:
        u = n+1
        d = 1
        for i in range(differ):
            u -= 1
            d += 1
        print("{}{}{}".format(u, tmp, d))
