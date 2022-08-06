n = int(input())

dp = [0]

dp.append(1)
dp.append(1)
dp.append(2)

if n <= 3:
    print(dp[n])
    exit()

for k in range(4, n+1):
    if k >= 4:
        dp.append(dp[k-1] + dp[k-2])

print(dp[n])


# 굿

