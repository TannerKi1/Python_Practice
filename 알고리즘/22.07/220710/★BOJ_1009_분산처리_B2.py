
T = int(input())

# 제곱하고, 뒷자리 수만 챙긴다!
for _ in range(T):
    a, b = map(int, input().split())
    a_int = int(a)
    b_int = int(b)
    for _ in range(b_int):
        if a_int < 10:
            a_int = a_int * a_int

    print(a_int)




3 9 7 1 3 9 7