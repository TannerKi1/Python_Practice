import math

M = int(input())
N = int(input())

array = [True for i in range(N+1)]
array[0] = False
array[1] = False

for i in range(2, int(math.sqrt(N + 1)) + 1):
    if array[i]:
        j = 2
        while i * j <= N:
            array[i * j] = False
            j += 1

prime_dict = dict()
total = 0

for x in range(M, N + 1):
    if array[x]:
        prime_dict[x] = 1
        total += x

if total != 0:
    print(total)
    print(list(prime_dict.keys())[0])
else:
    print(-1)















