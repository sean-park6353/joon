from collections import deque 
import sys
t=int(sys.stdin.readline())
# t=1
for i in range(1,t+1):
    # number,target=4,2
    # tmp=[1,2,3,4]
    number,target=map(int,sys.stdin.readline().split(' '))
    tmp=list(map(int,sys.stdin.readline().split(' ')))
    q=deque(enumerate(tmp))
    seq=0
    while q:
        flg=False
        tmp=q.popleft()
        for j in q:
            if tmp[1]<j[1]:
                q.append(tmp)
                flg=True
                break
        if flg==False:
            seq+=1
            if target==tmp[0]:
                break
    print(seq)