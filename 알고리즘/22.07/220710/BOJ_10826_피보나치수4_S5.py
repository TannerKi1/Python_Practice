n = int(input())

def fibo(n):
    a, b = 0, 1
    if n == 0:
        print(a)
    elif n == 1:
        print(b)

    elif n > 1:
        for i in range(n-1):
            a, b = b, a+b
        print(b)

fibo(n)

