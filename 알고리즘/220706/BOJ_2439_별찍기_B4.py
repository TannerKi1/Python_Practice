
N = int(input())

for k in range(1, N+1):
    a = " " * (N-k)
    b = "*" * k
    print(a, end='')
    print(b)

