

# 3 10 5
# 1 3 5 7 9

# K = 3 (1회 충전으로 갈 수 있는 거리)
# N = 10 (전체 칸의 개수)
# M = 5 (설치된 주유소의 위치 개수) [1, 3, 5, 7, 9], 설치 위치. 이 장소로 워프하게 됨.

# 시작은 0에서 시작함

T = int(input())

for tc in range(T):
    K, N, M = list(map(int, input().split()))

    charge_station = list(map(int, input().split()))

    current_bus = 0
    count = 0

    while current_bus + K < N:
        for step in range(K, 0, -1):
            if (current_bus + step) in charge_station:
                current_bus += step
                count += 1
        else:
            break
    print(count)
