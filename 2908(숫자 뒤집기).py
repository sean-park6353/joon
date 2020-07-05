
# 숫자 뒤집는방법
a = list(map(int, input().split()))
print((int(str(a[0])[::-1])) if int(str(a[0])[::-1]
                                    ) > int(str(a[1])[::-1]) else int(str(a[1])[::-1]))
