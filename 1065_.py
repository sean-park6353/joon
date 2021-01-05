
def hansoo(number):
    number = str(number)
    if len(number) <= 2:
        return True
    else:
        d = int(number[1])-int(number[0])
        if len(number) == 3:
            if int(number[2])-int(number[1]) != d:
                return False
            else:
                return True
        else:
            if int(number[2])-int(number[1]) != d:
                return False
            elif int(number[2])-int(number[3]) != d:
                return False
            else:
                return True


a = input()
cnt = 0
for i in range(1, int(a)+1):
    if hansoo(i) == True:
        cnt += 1
print(cnt)
