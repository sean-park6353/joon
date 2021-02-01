# def fibonacci(n):
#     if n == 0:
#         print('0')
#         return 0
#     elif n == 1:
#         print('1')
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)


# n = input()
# arr = []

# for i in range(int(n)):
#     arr.append(int(input()))

# print("="*15)
# fibonacci(arr[0])
# print("="*15)
# fibonacci(arr[1])
# print("="*15)
# fibonacci(arr[2])
import sys
n=int(sys.stdin.readline())
dp=[[0,0] for i in range(41)]

dp[0]=[1,0]
dp[1]=[0,1]
# print(dp)
for i in range(n):
    a=int(sys.stdin.readline())
    if a==0:
        print(1,0)
        continue
    for j in range(2,a+1):
        dp[j][0]=dp[j-2][0]+dp[j-1][0]
        dp[j][1]=dp[j-2][1]+dp[j-1][1]

    print(dp[a][0],dp[a][1])


