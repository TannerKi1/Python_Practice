N = list(map(int, input().split()))
H = N[0]
M = N[1]
M_2 = M - 45
# 45를 빼준다.

if M_2 >= 0:
    M_2 = M_2
    print(f'{H} {M_2}')

elif M_2 < 0:
    M_2 = 60 - abs(M_2)
    if H == 0:
        H = H + 23
    elif H != 0:
        H = H - 1
    print(f'{H} {M_2}')

