# 1. Greedy 문제로 추정
# 500,100, 50, 10 문제랑 다른 하나는...
# 나머지가 5, 3으로 조합으로 이루어진 최적을 나머지 0으로 찾아야하는 것.


N = int(input())

kilo = [5, 3]
count = 0

for sugar in kilo:
    count = count + N // sugar
    N = N % sugar

print(count)


