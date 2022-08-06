
A, B, C = map(int, input().split())

base = A
for i in range(B):
    if base < C:
        base *= A

    elif base >= C:
        base = base % C


print(base)