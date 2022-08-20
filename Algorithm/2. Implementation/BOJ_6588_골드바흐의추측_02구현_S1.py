# 빠른 입출력을 위해 input 대신 sys.stdin.readline사용
import sys
input = sys.stdin.readline

# 에라토스테네스의 체 구현하기, 0과 1은 소수가 아님을 사전에 선언하기
prime_number = [0] * (1000000)
prime_number[0] = 1
prime_number[1] = 1

# 소수만 남기고 소수의 배수는 모두 소수가 아님을 처리하기
for i in range(2, 1001):
    j = 2
    while i * j < 1000000:
        prime_number[i * j] = 1
        j += 1

# while문 안에 에라토스테네스의 체를 넣으면 while이 돌아갈 때마다 소수를 새로 갱신하게 된다.
# 따라서 에라토스테네스의 채를 만들 때에는 반드시 함수나 반복 문 밖에다 빼고 돌리도록 하자.

# while문을 돌리다가 0이 들어오면 반복문이 종료되게 된다.
while True:
    n = int(input())
    if n == 0:
        break

    for x in range(3, len(prime_number)):
        if prime_number[n] == 0 and prime_number[n - x] == 0:
            print(f'{n} = {x} + {n - x}')
            break






