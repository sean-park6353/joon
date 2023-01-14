from bisect import bisect_left
import sys
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

a=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
b=int(sys.stdin.readline())
brr=list(map(int,sys.stdin.readline().split()))

arr.sort()
answer=[]
for i in range(len(brr)):
    if BinarySearch(arr,brr[i])==-1:
        answer.append(0)
    else:
        answer.append(1)
print(*answer,sep='\n')


# 주석 색깔






