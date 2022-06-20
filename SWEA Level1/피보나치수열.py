
# 점화식으로 표현한 피보나치


def fibonacci_recursive(n):
    if n<= 1:
        return n

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)



print(fibonacci_recursive(10))



# 그냥 무식하게 적어보는 피보나치

#1

a = [1, 1]
for i in range(1, 9):
    b = a[i] + a[i-1]
    a.append(b)

print(a)


# 분명 점화식으로 나중에 업그레이드 할 수 있음.