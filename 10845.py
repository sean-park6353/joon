from collections import deque
import sys
n=int(sys.stdin.readline())
q=deque([])

for i in range(n):
    insert=list(map(str,sys.stdin.readline().strip().split(" ")))
    if len(insert)==2:
        q.append(int(insert[1]))
    else:
        if insert[0]=="pop":
            try:
                print(q.popleft())
            except :
                print(-1)
        elif insert[0]=="size":
            print(len(q))
        elif insert[0]=="empty":
            if q:
                print(0)
            else:
                print(1)
        elif insert[0]=="front":
            if q:
                print(q[0])
            else:
                print(-1)
        else:
            if q:
                print(q[-1])
            else:
                print(-1)
