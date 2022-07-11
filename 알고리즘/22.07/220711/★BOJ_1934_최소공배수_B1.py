T = int(input())

for x in range(T):
    A, B = map(int, (input().split()))
    A_yak = []
    B_yak = []
    for item in range(1, A+1):
        if A % item ==0:
            A_yak.append(item)

    for item in range(1, B+1):
        if B % item == 0:
            B_yak.append(item)

    C_yak = []
    for z in A_yak:
        if z in B_yak:
            C_yak.append(z)
    GDB = max(C_yak)
    print(int(GDB * A/GDB * B/GDB))

# 유클리드 호제법이 나오는 걸 보니까, 일반적으로 그냥 for문 돌리면 시간초과 뜨는 듯

