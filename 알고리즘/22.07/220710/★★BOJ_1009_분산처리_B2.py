import sys
T = int(input())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    ans = 1
    for i in range(1, b+1):
        if ans < 10:
            ans *= a
        elif ans >= 10:
            ans = (ans % 10) * a

    print(ans % 10)
# mod 값으로 곱하는 거 같은데...
# a1 3, 9, 27, 81


