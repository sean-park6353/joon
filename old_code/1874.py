from collections import deque
import sys
a = int(sys.stdin.readline())
arr = deque([])
for i in range(a):
    arr.append(int(sys.stdin.readline()))
stack = deque([1])
value = 2
flg = False
alen = len(arr)
slen = len(arr)
answer = "+"
for i in range(alen):
    while True:
        if len(stack) == 0:
            stack.append(value)
            answer += "+"
            value += 1
            continue
        if stack[-1] == arr[i]:
            stack.pop()
            break
        if stack[-1] > arr[i]:
            flg = True
            break
        if arr[i] < stack[-1]:
            stack.pop()
            answer += '-'
        stack.append(value)
        answer += "+"
        value += 1
    answer += '-'
    if flg == True:
        break
answerlen = len(answer)
if flg == True:
    sys.stdout.write('NO')
else:
    for i in range(answerlen):
        sys.stdout.write(answer[i])
        sys.stdout.write('\n')
