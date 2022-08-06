# import sys
# n, W = map(int, sys.stdin.readline().split())
# weight = [0]
# value = [0]
#
# for tc in range(n):
#     w, v = map(int, sys.stdin.readline().split())
#     weight.append(w)
#     value.append(v)
#
# K = [[0] * (W+1) for _ in range(n+1)]
#
# for i in range(1, n+1):
#     for w in range(1, W+1):
#
#         if weight[i] > w:
#             K[i][w] = K[i-1][w]
#
#         else:
#             K[i][w] = max(K[i-1][w - weight[i]] + value[i], K[i-1][w])
#
# print(K[n][W])

n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split()))) # 물건의 무게와 가치를 THING안에 저장하는 과정.

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]
        # thing 앞에 있는 게 무게고, 뒤에 있는 게 가치

        if j < w:   # 개별 j는 조금씩 커져가는 가방의 사이즈
            d[i][j] = d[i-1][j]  # i는 아이템 개수
        else: # 가방이 w보다 조금 더 큰 경우
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])