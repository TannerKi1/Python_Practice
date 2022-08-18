array = list(map(int, input()))


# 연산자를 넣는다는 건 어떻게 할 수 있을까?


dp = [0] * len(array)

dp[0] = array[0]

for i in range(1, len(array)):
    dp[i] = max(dp[i-1] + array[i], dp[i-1] * array[i])

print(max(dp))