t = int(input())
arr = []
answer = []

dp = [0] * 1000
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
for data in range(t):
    arr.append(int(input()))

for n in arr:
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    answer.append(dp[n])
    
for data in answer:
    print(data)