# A와 B가 가위바위보를 하였다.
#
# 가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
#
# A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.
#
#
#
# [입력]
#
# 입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.

T = list(map(int, input().split()))

A = T[0]
B = T[1]

if T[0] == T[1]:
    print("DRAW")

if T[0] == 1:
    if T[1] == 3:
        print("A")
    elif T[1] == 2:
        print("B")

elif T[0] == 2:
    if T[1] == 1:
        print("A")
    elif T[1] == 3:
        print("B")

elif T[0] == 3:
    if T[1] == 2:
        print("A")
    elif T[1] == 1:
        print("B")
