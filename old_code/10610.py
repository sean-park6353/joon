a = list(map(int, input().strip()))
a.sort(reverse=True)


if a[-1] == 0:  # 1의자리의 수가 0일때만 찾으면 된다.
    if sum(a) % 3 == 0:
        for i in a:
            print(i, end='')
    else:
        print(-1)
else:
    print(-1)
