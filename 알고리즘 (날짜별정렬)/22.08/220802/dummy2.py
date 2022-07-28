import math

n, m = map(int, input().split())

arr_ = [0] * (m+1)

for x in range(2, int(math.sqrt(m))+1):
    j = 2
    while x * j <= m:
        arr_[x * j] = 1
        j += 1

prime = []
for z in range(2, m+1):
    if arr_[z] == 0:
        prime.append(z)


print(prime)