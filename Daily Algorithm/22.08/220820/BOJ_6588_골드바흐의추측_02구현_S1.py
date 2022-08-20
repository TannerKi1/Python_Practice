# 에라토스테네스의 체 빠르게 구현
import sys
input = sys.stdin.readline

prime_number = [0] * (1000000)

for i in range(2, 1001):
    j = 2
    while i * j < 1000000:
        prime_number[i * j] = 1
        j += 1

while True:
    K = int(input())
    if K == 0:
        break

    for x in range(3, len(prime_number)):
        if prime_number[x] == 0 and prime_number[K - x] == 0:
            print(f'{K} = {x} + {K - x}')
            break





