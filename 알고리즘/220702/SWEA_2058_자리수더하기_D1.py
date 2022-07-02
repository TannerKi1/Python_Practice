
# 자리수 더하기

# 목표 : 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라


# 숫자를 받는다, 문자열로 바꾼다, 훑는다, 개별 값을 다 더한다.

T = int(input())

T_str = str(T)

array = []
count = 0

for x in T_str:
    array.append(int(x))

print(sum(array))

# list 내부의 값을 다 더하는 함수는 sum()