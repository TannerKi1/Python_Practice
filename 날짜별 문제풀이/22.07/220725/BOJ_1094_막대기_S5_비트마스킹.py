# 2**n승 알고 있으면 해결될듯?

N = int(input())

length = [64, 32, 16, 8, 4, 2, 1]

count = 0
for i in length:
    if i <= N:
        N = N % i
        count += 1
    if N == 0:
        break

print(count)
