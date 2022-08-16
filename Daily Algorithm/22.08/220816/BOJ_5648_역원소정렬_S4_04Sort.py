while True:
    A, B = map(int, input().split())
    if A == 0 & B == 0:
        break

    if A - B > B:
        B = A - B

    K = A - B

    up = 1
    down = 1
    for i in range(0, K):
        up *= (A - i)
        down *= i+1

    print(int(up / down))


