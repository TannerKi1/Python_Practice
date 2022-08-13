n = int(input())
dp = [0]
wine = [0]

for i in range(n):
    wine.append(int(input()))

dp.append(wine[1])

if n > 1:
    dp.append(wine[1]+wine[2])

for i in range(3, n+1):
    dp.append(max(dp[i-2] + wine[i], wine[i] + wine[i-1] + dp[i-3], dp[i-1]))

print(max(dp))
