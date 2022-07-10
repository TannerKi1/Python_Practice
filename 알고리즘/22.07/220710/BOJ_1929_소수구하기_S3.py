import math

M, N = map(int, input().split())
arr = [0] * N
arr[0] = 1

for x in range(2, int(math.sqrt(N))+1):
    j = 2
    while x * j <= N:
        arr[x * j -1] = 1
        j += 1

for k in range(M, N+1):
    if arr[k-1] == 0:
        print(k)



