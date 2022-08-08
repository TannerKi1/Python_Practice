# 1260원을

# 500원, 100원, 50원, 10원으로 거슬러 주기

N = int(input())
coin_types = [500, 100, 50, 10]

count = 0

for coin in coin_types:
    if N >= coin:
        count = N // coin
        N %= coin

print(count)

# 배수 단위가 아니라면 DP로 넘어가게 된다.
