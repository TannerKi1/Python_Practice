
# 2차원 리스트 초기화 하는 법


num1, num2 = list(map(int, input().split(',')))

m = int(num1) # 전체 []가 몇 개인지
n = int(num2) # []안에 들어가는 숫자가 몇 개인지

b = []

for x in range(m):
    c = []
    for y in range(n):
        c.append(x*y)
    b.append(c)

print(b)
