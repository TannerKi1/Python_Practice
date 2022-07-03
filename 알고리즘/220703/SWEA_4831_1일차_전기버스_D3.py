# 나눗셈으로 숫자 받아가자

T = int(input())

for x in range(1, T+1):
    N = int(input())
    arr = [0] * 10
    num = int(input())

    for _ in range(1, N+1):
        b = num % 10
        arr[b] += 1
        num = num // 10

    if arr.count(max(arr)) == 1:
        print(f'{arr.index(max(arr))} {max(arr)}')

    else:
        []
