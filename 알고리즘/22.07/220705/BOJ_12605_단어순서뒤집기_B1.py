import sys
N = int(input())

for x in range(1, N+1):
    k = list(map(str, sys.stdin.readline().split()))
    k_r = k[::-1]
    print(f'Case #{x}: ', end='')
    for j in k_r:
        print(j, end=' ')
    print()
