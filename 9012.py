n = int(input())
arr = []
for i in range(n):
    arr.append(input())
stack = []
result = []
for i in range(n):
    for j in range(len(arr[i])):
        if arr[i][j] == '(':
            stack.append('(')
        elif arr[i][j] == ')':
            try:
                stack.pop()
            except:
                result.append('NO')
                break
        if j == len(arr[i])-1:
            if len(stack) != 0:
                result.append('NO')
            else:
                result.append('YES')
    stack.clear()
for i in result:
    print(i)

# arr = []
# try:
#     arr.pop()
# except:
#     print('아이고')
