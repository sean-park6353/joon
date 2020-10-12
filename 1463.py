x = int(input())
cnt = 0

while x != 1:
    if (x-1) % 3 == 0:
        x -= 1
        cnt += 1
    if (x-1) % 2 == 0:
        x -= 1
        cnt += 1
    if x % 3 == 0:
        x //= 3
        cnt += 1
    if x % 2 == 0:
        x //= 2
        cnt += 1

print(cnt)
