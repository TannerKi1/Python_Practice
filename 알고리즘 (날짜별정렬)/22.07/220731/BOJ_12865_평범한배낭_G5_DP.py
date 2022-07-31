import sys
n, W = map(int, sys.stdin.readline().split())
weight = []
value = []

for tc in range(n):
    w, v = map(int, sys.stdin.readline().split())
    weight.append(w)
    value.append(v)

K = [[0] * (W+1) for _ in range(n+1)]

def knapsack():
    for i in range(n+1):
        K[i][0] = 0 # 가방 무게가 0인 경우

    for w in range(W+1):
        K[0][w] = 0 # 물건이 0개인 경우

    for i in range(1, n):
        for w in range(1, W):
            if weight[i] > W:
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(K[i-1][W - weight[i]] + value[i], K[i-1][w])\

    return K[n][w]

print(knapsack())
print(K)

