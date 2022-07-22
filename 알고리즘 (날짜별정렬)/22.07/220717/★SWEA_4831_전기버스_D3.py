

# 3 10 5
# 1 3 5 7 9

# K = 3 (1회 충전으로 갈 수 있는 거리)
# N = 10 (전체 칸의 개수)
# M = 5 (설치된 주유소의 위치 개수) [1, 3, 5, 7, 9], 설치 위치. 이 장소로 워프하게 됨.

# 시작은 0에서 시작함

T = int(input())

for TC in range(T):
    K, N, M = list(map(int, input().split()))

    charge_station = list(map(int, input().split()))

    current = 0
    count = 0

    while current + K < N:
        for step in range(K, 0, -1):
            if (current + step) in charge_station:
                current += step
                count += 1
                break # 빠져나가서 다시 k부터 돌게 된다. while에 걸리니까
                # 만약 if문에 안 걸리면 K값이 -1로 빠지면서 다시 for문을 돌게된다.

        else:
            count = 0
            break
    print(f'#{TC+1} {count}')

# 최대 K칸을 갈 수 있으면, K-1, K-2를 갈 수도 있기 때문에 이건 for문을 돌려야한다. 대신에 가장 멀리 가는 거니까 K에서부터 역으로 -1로 접근하는 것