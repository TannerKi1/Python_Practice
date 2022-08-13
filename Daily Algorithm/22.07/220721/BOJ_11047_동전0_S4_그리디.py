# 1. Greedy 대표적인 문제

N, K = map(int, input().split())
money_2 = []
for _ in range(N):
    money_2.append(int(input()))

money_2.sort(reverse = True)
count = 0

for coin in money_2:
    if K >= coin: # 등호 조심!
        add_count = K // coin
        count += add_count
        K %= coin

print(count)
