n = int(input())
score = []
cnt = []
for i in range(n):
    score.append(input())
    cnt.append(0)
for i in range(n):
    plus = 1
    for j in range(len(score[i])):
        if score[i][j] == 'O':
            cnt[i] = cnt[i]+plus
            plus = plus+1
        else:
            plus = 1
for i in range(n):
    print(cnt[i])
