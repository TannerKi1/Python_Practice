n = int(input())
dp = [0]
wine = [0]

for i in range(n):
    wine.append(int(input()))

dp.append(wine[1])

if n > 1:
    dp.append(wine[1]+wine[2])

for i in range(3, n+1):
    dp.append(max(dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i], dp[i-1]))

print(max(dp))

# BOJ_2579와의 차이점은, 마지막 포도주를 꼭 마셔야 할 필요가 없다는 점이다. 따라서 max 안의 옵션이 3개까지 늘어나게 된다.


