N = int(input())
arr_2 = list(map(int, input().split()))
arr = arr_2[::-1]

dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))
