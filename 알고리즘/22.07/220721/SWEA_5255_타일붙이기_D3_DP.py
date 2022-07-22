T = int(input())

dp = [0] * 31

dp[1] = 1
dp[2] = 3
dp[3] = 6

for i in range(1, T+1):
    k = int(input())
    for x in range(4, 31):
        dp[x] = dp[x-1] + 2*dp[x-2] + dp[x-3]

    print(f'#{i} {dp[k]}')

