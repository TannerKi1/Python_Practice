n = int(input())
times = list(map(int, input().split()))

dp = [0]
times.append(0)

times.sort()

dp.append(times[1])

for x in range(2, n+1):
    dp.append(dp[x-1] + times[x])

print(sum(dp))

# 굿. dp에 append 하는 식으로 풀어내자

