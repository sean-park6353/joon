
while True:
    stack = []
    flg = True
    sentence = input()
    if sentence == '.':
        break
    for i in sentence:
        if i == ')':
            if len(stack) == 0:
                flg = False
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == ']':
            if len(stack) == 0:
                flg = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)

    if flg == False:
        print('no')
        continue
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
