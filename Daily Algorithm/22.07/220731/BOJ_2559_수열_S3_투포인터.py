import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

num_arr = sum(arr[0:k])
dp = [num_arr]

for i in range(1, n-k+1):
    dp.append(dp[i-1] - arr[i-1] + arr[i-1+k])

print(max(dp))


# 누적값을 저장한 상태에서 앞 뒤로 1개씩만 불러오면 된다.

