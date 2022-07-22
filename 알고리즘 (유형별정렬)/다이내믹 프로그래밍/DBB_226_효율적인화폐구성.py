n, m = map(int, input().split())

dp = [10001] * (m+1)
coin = []

for _ in range(n):
    coin.append(int(input()))

dp[0] = 0

for i in range(n):
    for j in range(coin[i], m+1):
        if dp[j - coin[i]] != 10001:
            dp[j] = min(dp[j], dp[j-coin[i]] +1)


if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

