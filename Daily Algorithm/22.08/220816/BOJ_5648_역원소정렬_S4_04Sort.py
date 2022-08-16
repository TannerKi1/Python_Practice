from math import comb


while True:
    A, B = map(int, input().split())
    if A == 0 & B == 0:
        break

    print(comb(A, B))


