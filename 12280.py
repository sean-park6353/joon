t = int(input())
for i in range(1, t+1):
    Alex = []
    Bob = []
    Aindex = []
    Bindex = []
    n = int(input())
    tmp = list(map(int, input().split(" ")))
    for j in range(len(tmp)):
        if tmp[j] % 2 == 0:
            Bob.append(tmp[j])
            Bindex.append(j)
        else:
            Alex.append(tmp[j])
            Aindex.append(j)
    # print(Aindex)
    # print(Bindex)
    Alex = sorted(Alex)
    Bob = sorted(Bob, reverse=True)
    # print("Alex: ", Alex)
    # print("Bob: ", Bob)
    for j in range(len(Alex)):
        tmp[Aindex[j]] = Alex[j]
    for j in range(len(Bob)):
        tmp[Bindex[j]] = Bob[j]
    print("Case #%d:" % i, *tmp, end=' ')
    print()
