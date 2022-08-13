N, K = map(int, input().split())

d = [0] * (N+1)

for i in range(2, N+1):
    d[i] = d[i-1] + 1

    if i % K == 0:
        d[i] = min(d[i], d[i // K] + 1)

    # d[4]가 처음에는 d[3] + 1을 거려 3으로 세팅되었다가
    # if문에 걸리면서  min(3, 1)에 걸리면서 1로 초기화 완료
    # 그 다음 d[5]는 d[4]값을 받게 됨.

print(d[N])

