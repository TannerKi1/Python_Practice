
N = int(input())


b = [i for i in range(1, N+1) if N % i == 0]

for x in b:
    print(x, end=' ')