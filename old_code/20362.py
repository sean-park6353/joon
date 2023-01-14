n, s = map(str, input().split(" "))
n = int(n)
answer = ""
log = []
for i in range(n):
    log.append(list(map(str, input().split(' '))))

for i in range(n):
    if s == log[i][0]:
        answer += log[i][1]

print(log)
cnt = 0
log = log[::-1]
print(log)
for i in range(1, n):
    if answer == log[i][1]:
        cnt += 1

print(cnt)
