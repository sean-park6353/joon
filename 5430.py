import sys
from collections import deque
t=int(sys.stdin.readline().strip())
for i in range(t):
    flg=1
    func=list(map(str,sys.stdin.readline().strip()))
    n=int(sys.stdin.readline().strip())
    tmp=sys.stdin.readline().strip()
    if n==0:
        sys.stdout.writelines("error")
        sys.stdout.writelines("\n")
        continue
    arr=deque([])
    # arr=[]
    number=""
    for data in tmp:
        if data.isnumeric():
            number+=data
        elif data=="," or data=="]":
            arr.append(int(number))
            number=""
        
    for j in func:
        if j=="R":
            if len(list(set(arr)))!=1:
                arr.reverse()
        else:
            try:
                arr.popleft()
            except :
                sys.stdout.writelines("error")
                sys.stdout.writelines("\n")
                flg=0
                break
    if flg==0:
        continue
    result="["
    for i in range(len(arr)):
        if i!=len(arr)-1:
            result+=str(arr[i])+","
        else:
            result+=str(arr[i])
    result+="]"
    sys.stdout.writelines(result)
    sys.stdout.writelines("\n")

