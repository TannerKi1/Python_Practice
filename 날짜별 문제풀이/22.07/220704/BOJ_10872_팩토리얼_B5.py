N = int(input())

def fac(N):
    if N == 0:
        return 1
    else:
        return fac(N-1) * N

print(fac(N))



