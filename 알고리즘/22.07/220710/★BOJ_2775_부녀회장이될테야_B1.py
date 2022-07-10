# 그림을 그려보면 대각선 두 개 호수의 합임을 확인할 수 있다.

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    array = [[0] * n for _ in range(k+1)]
    array[0][0] = 1

    for K in range(0, k+1): # k는 층수]
        for N in range(0, n):
            if K == 0:
                array[K][N] = N+1
            elif K != 0:
                if N == 0:
                    array[K][N] = 1
                elif N != 0:
                    array[K][N] = array[K][N-1] + array[K-1][N]

    print(array[k][n-1])




