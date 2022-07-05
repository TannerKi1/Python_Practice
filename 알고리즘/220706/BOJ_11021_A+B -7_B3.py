import sys
T = int(input())
for _ in range(T+1):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B)