T = int(input())

for x in range(T):
    arr = [1] * 15000

    for i in range(2, 101):
        for j in range(i+i, 10001, i):
            arr[j] = 0

    even = int(input())
    half = even // 2

    for p in range(half, 1, -1):
        if arr[(even - p)] == 1 and arr[p] == 1:
            print(p, even-p)
            break












