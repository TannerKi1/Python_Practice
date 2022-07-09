import math

T = int(input())

numbers = list(map(int, input().split()))

count = 0

for x in numbers:
    if x == 1:
        continue
    c_s = 0
    for j in range(2, int(math.sqrt(x)) + 1):
        if x % j == 0:
            c_s = 1
    if c_s == 0:
        count += 1


print(count)





