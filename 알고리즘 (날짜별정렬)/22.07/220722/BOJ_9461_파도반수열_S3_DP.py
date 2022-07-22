T = int(input())
for x in range(T):
    n = int(input())

    dp = [0, 1, 1, 1, 2, 2, 3]


    for k in range(7, n+1):
        dp.append(dp[k-1] + dp[k-5])

    print(dp[n])

# 점화식이 반이다.