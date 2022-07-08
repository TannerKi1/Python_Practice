
T = int(input())

# 제곱하고, 뒷자리 수만 챙긴다!
for _ in range(T):
    a, b = input().split()
    a_int = int(a)
    b_int = int(b)
    for _ in range(b_int):
        a_int = (a_int * a_int) % 10
    print(a_int)




