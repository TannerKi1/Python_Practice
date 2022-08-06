
n = int(input())

for x in range(n):
    k = int(input())
    dp = [0]
    dp.append(1)
    dp.append(2)
    dp.append(4)
    if k <= 3:
        print(dp[k])

    if k >= 4:
        for z in range(4, k+1):
            dp.append(dp[z-1] + dp[z-2] + dp[z-3])
        print(dp[-1])


# 점화식 잘 세웠음. 굿