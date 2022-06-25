
# 아이디어 끄적거리기
# 입력값이 이름, 나이가 구분되어서 들어오면 어떻게 나눠서 저장할 것인지?
# input 으로 이름을 받고, input2로 나이를 받아서 각각 배정하면...?
# 홍길동은 홍길동으로 받는데, 2022년 20살이면, 이후 100살에는 2022 + 100-x를 리턴?

name = input("이름을 입력해주세요: ")
age = input("나이를 입력해주세요: ")
this_year = int(2022)
b = int(100)-int(age)

def age_calc(name, age):
    print (f'{name}(은)는 {this_year+b-3}년에 100세가 될 것입니다.')


age_calc(name, age)

# 하지만 이 풀이는 '내장함수'를 이용하지 않았지.

# 날짜를 구하는 내장함수에는 'datetime()이라는 것이 있다.