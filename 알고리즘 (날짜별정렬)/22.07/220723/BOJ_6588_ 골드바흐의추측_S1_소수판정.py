# 소수 리스트 만들기

arr = [0] * 1000000
import sys

for i in range(2, 1001):
    if arr[i] == 0:
        for j in range(i+i, 1000000, i):
            arr[j] = 1

arr[0] = 1
arr[1] = 1

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
#
    for i in range(3, len(arr)):
        if arr[i] == 0 and arr[n-i] == 0:
            print(f'{n} = {i} + {n-i}')
            break


# 0이 들어올 때까지 while문 돌리는 법을 외워놓자...!