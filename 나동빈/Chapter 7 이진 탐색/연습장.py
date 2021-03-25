arr=[4,1,15,20,9,21]
arr.sort()
target=4
start=0
end=len(arr)-1
middle=len(arr)//2
while start<end:
    if target<arr[middle]:
        end=middle
        middle=(start+end)//2
    elif target>arr[middle]:
        start=middle
        middle=(start+end)//2
    else:
        break