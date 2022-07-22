
# 정수 N을 받으면 정수 N까지의 값이 리턴되고 이걸 key로 받고


# 그 정수의 제곱값을 value로 받는 딕셔너리 만들기


T = int(input())

b = [i for i in range(1, T+1)]

dic = {}

for x in b:
    dic[x] = x*x
print(dic)

