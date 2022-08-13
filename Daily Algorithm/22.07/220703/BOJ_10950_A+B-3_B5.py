import sys
T = int(input())

for i in range(1, T+1):
    arr = list(map(int, sys.stdin.readline().split()))
    print(arr[0]+arr[1])
