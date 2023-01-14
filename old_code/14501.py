n = int(input())
cost = []
money = []
for i in range(n):
    a, b = map(int, input().split(' '))
    cost.append(a)
    money.append(b)

earn = []

for i in range(n):
    cnt = cost[i]
    earn.append(money[i])
    for j in range(n):
        cnt -= 1
        if cnt == 0:
            earn.append(money[j])
            cnt = cost[i]
print(earn)
