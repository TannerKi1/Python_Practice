
# 피보나치 점화식을 복습해볼 수 있는 좋은 기회...!

array = []
x = int(input("피보나치 숫자 구하기: "))

def fibo(n):
    if n <= 2:
        return 1

    else:
        return fibo(n-2) + fibo(n-1)


for k in range(1, x+1):
    array.append(fibo(k))

print(array)




