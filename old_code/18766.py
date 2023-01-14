T = int(input())
for i in range(T):
    arr = []
    n = int(input())
    for j in range(2):
        arr.append(list(map(str, input().split(' '))))
    arr[0].sort()
    arr[1].sort()
    if arr[0] == arr[1]:
        print("NOT CHEATER")
    else:
        print("CHEATER")
