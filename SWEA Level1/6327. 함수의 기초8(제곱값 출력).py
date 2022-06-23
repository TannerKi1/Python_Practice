


# 이 문제의 핵심은 ,로 구분되어 나누어 들어오는 값을 어떻게 각각 받아서 처리할 것인가?

# 이 때 바로 map으로 구분해서 받는 걸 쓰는 것!!!!!!!!!!!! ★

# input().split('a')의 해석
# input()으로 들어온 값을 'a'를 기준으로 나누어라.
# 2, 3이 들어왔으니, 2 / 3으로 나뉘게 됨!!! ... 이제야 이해했네



# 제곱의 기호는 **

num1, num2 = list(map(int, input().split(',')))

def square_num(n):
    return n**2

print(f'{num1} => {square_num(num1)}')
print(f'{num2} => {square_num(num2)}')


