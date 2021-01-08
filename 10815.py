import sys
a = int(sys.stdin.readline())
arr = set(list(map(int, sys.stdin.readline().split(' '))))
b = int(sys.stdin.readline())
brr = list(map(int, sys.stdin.readline().split(' ')))
for i in brr:
    if i in arr:
        sys.stdout.write('1')
    else:
        sys.stdout.write('0')
    sys.stdout.write(' ')
