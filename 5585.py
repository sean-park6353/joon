n = int(input())

n = 1000-n
cnt = [0]*6
dong = [500, 100, 50, 10, 5, 1]
i = 0
while n > 0 or i <= 5:
    cnt[i] = int(n/dong[i])
    n = n-dong[i]*int(n/dong[i])
    # print(cnt[i])
    i += 1


print(sum(cnt))
