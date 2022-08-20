import sys
import math
input = sys.stdin.readline

arr = [0] * 1001002

for i in range(2, 1002):
    j = 2
    while i * j <= 1000003:
        arr[i * j] = 1
        j += 1

N = int(input())

if N == 1:
    print(2)
    exit()

if N >= 2:
    for i in range(N, 2000000):
        if arr[i] == 0:
            if str(i) == str(i)[::-1]:
                print(i)
                exit()

