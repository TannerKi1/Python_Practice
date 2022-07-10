# 그림을 그려보면 대각선 두 개 호수의 합임을 확인할 수 있다.

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    array = [[0] * n for _ in range(k)]

    array[0][0] = 1
    for K in range(0, k):
        array[0][N] = N
        for N in range(0, n):
            array[K][0] = K
            array[K+1][N+1] = array[K+1][N] + array[K][N+1]

    print(array[k][n])




