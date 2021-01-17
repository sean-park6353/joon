t = int(input())
for i in range(1, t+1):
    Alex = []
    Bob = []
    Aindex = []
    Bindex = []
    n = int(input())
    tmp = list(map(int, input().split(" ")))
    for j in tmp:
        if j == 0:
            continue
        if j % 2 == 0:
            Bob.append(j)
            Bindex.append(tmp.index(j))
        else:
            Alex.append(j)
            Aindex.append(tmp.index(j))
    # print("Alex: ", Alex)
    # print("Bob: ", Bob)
    Alex = sorted(Alex)
    Bob = sorted(Bob, reverse=True)
    for j in range(len(Alex)):
        tmp[Aindex[j]] = Alex[j]
    for j in range(len(Bob)):
        tmp[Bindex[j]] = Bob[j]
    print("Case #%d:" % i, *tmp, end=' ')
    print()
