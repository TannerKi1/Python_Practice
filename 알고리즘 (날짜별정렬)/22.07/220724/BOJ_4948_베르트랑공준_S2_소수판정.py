import math
import sys

arr = [0] * 246913

for i in range(2, 497):
    for j in range(i+i, 246913, i):
        arr[j] = 1

arr[0] = 1
arr[1] = 1


def prime(n):
    count = 0
    for i in range(1, n+1):
        if arr[i] == 0:
            count += 1
    return count

while True:
    x = int(input())
    if x == 0:
        break
    else:
        print(prime(2*x) - prime(x))







