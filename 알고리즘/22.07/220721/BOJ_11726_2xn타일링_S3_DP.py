dp = [0] * 1001

dp[1] = 1
dp[2] = 2

k = int(input())

for x in range(3, 1001):
    dp[x] = (dp[x-1] + dp[x-2]) % 10007

print(dp[k])