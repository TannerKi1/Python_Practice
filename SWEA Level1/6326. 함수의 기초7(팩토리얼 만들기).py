
# 1단계로 푸는 법

def fac(n):
    result1 = 1
    for i in range(1, n+1):
        result1 *= i

    return result1

print(fac(2))

# 점화식으로 푸는 법


def fac_2(n):
    if n <= 1:
        return 1
    return n * fac_2(n-1)


print(fac_2(4))