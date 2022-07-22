N = int(input())

dp = [0] * (N+1)

dp[1] = 1
dp[2] = 3

for n in range(3, N+1):
    dp[n] = dp[n-1] + 2*dp[n-2]

print(dp[N])


# 결국 점화실 잘 세우면 장땡이다.