# 0부터 올리지만 말고, 카운트를 역으로 해서 내려오는 것도 생각해보자.

N = int(input())

first = 666

while N != 0:
    if '666' in str(first):
        N -= 1
    if N == 0:
        break  # 0일때 break 끝내고 나와야 +1이 되지 않은 값을 볼 수 있다. 그전에는 계속 first가 증가해야하고.

    first += 1

print(first)

