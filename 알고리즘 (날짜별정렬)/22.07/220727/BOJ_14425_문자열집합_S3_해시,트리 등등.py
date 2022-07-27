N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())

set_S = set(S)

count = 0
for _ in range(M):
    if input() in set_S:
        count += 1

print(count)


# 이게 되네;