a=int(input())
dp=[0,1]
for i in range(2,a+1):
    dp.append(dp[i-1]+dp[i-2])
print(dp[a])