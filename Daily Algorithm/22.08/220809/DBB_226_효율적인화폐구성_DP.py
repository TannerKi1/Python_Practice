# 설탕배달 문제랑 사실상 동일함

n, m = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

d = [9999] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(coin[i], m+1):
        d[j] = min(d[j], d[j - coin[i]] + 1)

if d[m] != 9999:
    print(d[m])

else:
    print(-1)