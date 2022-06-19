import math

x = int(input("판별을 원하는 소수를 넣어주세요: "))



#1부터 자기보다 작은 숫자로 나눠서 나머지가 0이 되는지를 판단한다


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return f'{x}는 소수가 아닙니다'

        return True

print(is_prime_number(x))

