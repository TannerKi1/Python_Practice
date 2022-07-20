import math

N = int(input())

arr_1 = [0] * N
arr_2 = [0] * 2 * N


for x in range(2, int(math.sqrt(N))-1):
    if N % x != 0:
        j = 2
        while x*j <= N:
            arr_1[x*j] = 1
            j += 1

for i in range(2, N):
    if arr_1[i] == 0:
        print(i)

