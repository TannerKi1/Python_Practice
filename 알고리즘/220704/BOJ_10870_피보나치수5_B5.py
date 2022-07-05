n = int(input())

a = 0
b = 1

for _ in range(1, n):
    a, b = b, a+b

print(b)

# 점화식보다 시간 복잡도가 몹시 낮음.
# 점화식은 2**n, 이건 n
