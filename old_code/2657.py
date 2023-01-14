n = int(input())
num = []
alpha = []
tmp = []
for i in range(n):
    tmp.append(input().split())
    num.append(int(tmp[i][0]))
    alpha.append(list(map(str, tmp[i][1])))


for i in range(n):
    for j in range(len(alpha[i])):
        print(alpha[i][j]*num[i], end='')
    print()
