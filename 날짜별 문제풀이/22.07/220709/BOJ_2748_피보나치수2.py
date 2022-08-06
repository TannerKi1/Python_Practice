
n = int(input())

def fibo(n):
    a, b = 0, 1
    # 밑에서 a, b 형식을 사용할거라면 여기에도 a, b로 정의해줬어야함.
    # 그냥 분리해서 정의하면 값이 텀을 두고 바뀌기 때문에 문제가 생김.
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        for _ in range(n-1):
            a, b = b, a+b
        return b

print(fibo(n))
