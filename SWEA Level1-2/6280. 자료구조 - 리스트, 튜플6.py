# 약수를 추가하는 리스트
# 이건 쉽게 할 수 있을듯

a = []

b = int(input("약수가 궁금한 숫자를 입력해주세요: "))
c = 1

for x in range(1, b+1):
    if b % x == 0:
        a.append(x)

print(a)