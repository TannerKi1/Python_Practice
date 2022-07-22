import time
start = time.time()

n = int(input())
dp = []

while len(dp) < 1000:
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                dp.append(2**i * 3**j * 5**k)

dp.sort()

print(dp[n-1])
print(f'time: {time.time()-start}')

# 2초가 넘어가기 때문에 시간제한 초과하게 됨. DP로 풀어야 1초 밑으로 들어올 수 있다.

# DP로 작성한 풀이를 아래에 적어보자.

