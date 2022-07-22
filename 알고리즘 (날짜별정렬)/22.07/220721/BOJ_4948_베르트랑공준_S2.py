import math
import sys



def prime_number(n):
    arr = [0] * 246913

    for i in range(2, int(math.sqrt(n))+1):
        if arr[i] == 0:
            j = 2
            while i * j <= n:
                arr[i*j] = 1
                j += 1

    arr_1 = []

    for i in range(2, n+1):
        if arr[i] == 0:
            arr_1.append(i)

    return len(arr_1)

while True:
    num = int(input())
    print(prime_number(num*2) - prime_number(num))
    if num == 0:
        break












