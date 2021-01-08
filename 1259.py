s = "1"
while True:
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[-1-i] == s[i]:
            cnt += 1
    if s == "0":
        break
    if cnt == len(s):
        print('yes')
    else:
        print("no")
