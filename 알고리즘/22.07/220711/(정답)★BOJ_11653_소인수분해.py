# 소인수분해는 다른 로직을 사용해야함

# 에라토스테네스의... 그거와는 다른...

N = int(input())

d = 2

while N >= d:
    if N % d == 0:
        print(d)
        N = N / d
    else:
        d += 1

