N = int(input())

def fibon(N):
    if 1 <= N <= 2:
        return 1
    elif N == 0:
        return 0
    else:
        return fibon(N-1) + fibon(N-2)

print(fibon(N))