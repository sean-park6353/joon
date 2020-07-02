# 알파벳 찾기

S = input()

arr = []
alpha = []
dex = []


for i in range(26):
    alpha.append(chr(i+97))


for i in range(len(alpha)):
    for j in range(len(S)):
        if alpha[i] == S[j]:
            dex.append(S.find(S[j]))
            break
    if S.find(alpha[i]) == -1:
        dex.append(-1)

for i in range(len(dex)):
    print(dex[i], end=" ")
