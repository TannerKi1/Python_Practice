# 다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아
#
#
# 이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.

# 입력
# 2, 3, 4, 5


import math


def calc():
    a = list(map(int, input().split(',')))
    b = [round(2*k*math.pi, 2) for k in a]
    for x in b[:-1]:
        print(x, end=", ")
    print(b[-1])

calc()

# , 가 붙으면 그 직전까지만 돌리고,


