T = int(input())

import sys

for k in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{k}: {A+B}')