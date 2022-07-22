import time

# SOL(1)
# start = time.time()
#
# n = int(input())
# dp = []
#
# while len(dp) < 1000:
#     for i in range(0, 10):
#         for j in range(0, 10):
#             for k in range(0, 10):
#                 dp.append(2**i * 3**j * 5**k)
#
# dp.sort()
#
# print(dp[n-1])
# print(f'time: {time.time()-start}')

# 2초가 넘어가기 때문에 시간제한 초과하게 됨. DP로 풀어야 1초 밑으로 들어올 수 있다.
# 2, 3, 4, 5로 출발하는 건 알겠는데 어떻게 해야 14이런 애들을 걸러낼 수 있을까?
start = time.time()

n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    ugly[l] = min(next2, next3, next5)
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

    print(next2, next3, next5)

print(ugly[n-1])


