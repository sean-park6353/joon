# n = input()
# arr = []


# print(arr)
# n = int(n)
# tmp = []
# for i in range(size):
#     z = int(n/arr[size-1-i])
#     n = n-z*(10**(size-i-1))
#     tmp.append(z)


#! 위에는 구린 코드
n = input()
size = len(n)
arr1 = []
arr2 = []
for i in range(len(n)):
    arr1.append(1*(10**i))


def divide(s):
    tmp = []
    for i in range(len(s)):
        tmp.append(int(s[i:i+1]))
    return tmp


cnt = 0
arr2 = divide(n)
for i in range(arr1[size-1]*(arr2[0]-1), int(n)):
    cnt += 1
    if i+sum(divide(str(i))) == int(n):
        print(i)
        break


if cnt >= int(n):
    print(0)
