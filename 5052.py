import sys
T = int(sys.stdin.readline())
for i in range(1, T+1):
    answer = False
    n = int(sys.stdin.readline())
    arr = []
    for j in range(n):
        arr.append(sys.stdin.readline().strip('\n'))
    arr.sort()
    for j in range(n-1):
        if arr[j] == arr[j+1][0:len(arr[j])]:
            answer = True
            break
    if answer == True:
        sys.stdout.write('NO\n')
    else:
        sys.stdout.write('YES\n')
