T = int(input())

for _ in range(T):
    N = int(input())

    arr = [[] for _ in range(N+1)]
    arr_2 = list(map(int, input().split()))


# 오전에 배운 그래프는 무향 그래프일 경우에만 사용 가능하다.