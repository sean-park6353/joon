# import copy
# a=int(input())
# arr=list(map(int,input().split()))
# b=int(input())
# brr=list(map(int,input().split()))
import copy
a=10
arr=[6,3,2,10,10,10,-10,-10,7,3]
b=8
brr=[10,9,-5,2,3,4,5,-10]
tmp=copy.deepcopy(arr)
answer=[0]
for target in brr:
    start=0
    end=len(tmp)-1
    while start<=end:
        middle=(start+end)//2
        if target<tmp[middle]:
            end=middle-1
        elif target>tmp[middle]:
            start=middle+1
        else:
            tmp.pop(middle)
            break