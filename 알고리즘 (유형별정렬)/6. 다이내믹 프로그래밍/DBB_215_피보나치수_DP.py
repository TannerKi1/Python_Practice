import time
start = time.time()
n = int(input())

# sol. 1

# dp = [0] * (n+1)
# dp[0] = 1
# dp[1] = 1
#
#
# for i in range(2, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
#
# print(dp[n])
# print(f'{time.time() - start}')


# 시간이 2초를 넘지 않는 것을 알 수 있다.
# 만약 같은 원리를 재귀함수로 구현한다면?

# sol. 2

def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(n))
print(f'{time.time() - start}')

# 50까지만 가도 고장이 난다.