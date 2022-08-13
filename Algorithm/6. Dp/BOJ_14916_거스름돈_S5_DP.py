n = int(input())

coin = [2, 5]

d = [20001] * (100001)
d[0] = 0

for i in range(len(coin)):
    for j in range(1, 100001):
        if d[j - coin[i]] != 20001:
            d[j] = min(d[j], d[j - coin[i]] + 1)

if n == 0:
    print(-1)
    exit()

if n >= 1:
    if d[n] == 20001:
        print(-1)
        exit()

    else:
        print(d[n])
        exit()

# 백준 2%에서 안 올라가는 이유는?