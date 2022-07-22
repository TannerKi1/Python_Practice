# 0부터 올리지만 말고, 카운트를 역으로 해서 내려오는 것도 생각해보자.

N = int(input())

first = 666

while N != 0:
    if '666' in str(first):
        N -= 1
    if N == 0:
        break
    first += 1

print(first)

