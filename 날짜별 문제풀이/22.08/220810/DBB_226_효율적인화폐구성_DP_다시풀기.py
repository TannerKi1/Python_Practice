N, M = map(int, input().split())

coin = []

for _ in range(N):
    coin.append(int(input()))

d = [9999] * (M + 1)
d[0] = 0
for i in range(len(coin)):
    for j in range(coin[i], M+1): # j의 시작점이 coin[i]라는거, 그리고 작은 코인부터 나열되어야한다는거
        d[j] = min(d[j], d[j - coin[i]] + 1)

if d[M] != 9999:
    print(d[M])
else:
    print(-1)

