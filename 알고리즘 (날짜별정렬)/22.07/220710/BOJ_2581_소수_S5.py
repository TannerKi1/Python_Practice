# 에라토스테네스의 채

import math

M = int(input())
N = int(input())
sosu_M = []
sosu_N = []

arr = [0] * (M+1)
arr_2 = [0] * (N+1)

for i in range(2, int(math.sqrt(M))+1):
    if arr[i] == 0:
        j = 2
        while i * j <= M:
            arr[i * j] = 1
            j += 1

for i in range(2, M):
    if arr[i] == 0:
        sosu_M.append(i)

for i in range(2, int(math.sqrt(N))+1):
    if arr_2[i] == 0:
        j = 2
        while i * j <= N:
            arr_2[i * j] = 1
            j += 1

for i in range(2, N+1):
    if arr_2[i] == 0:
        sosu_N.append(i)

final_arr = list(set(sosu_N) - set(sosu_M))

if len(final_arr) == 0:
    print(-1)
else:
    print(sum(final_arr))
    print(min(final_arr))


