
N = int(input())
M = N

count = 0

while True:
    a = M // 10
    b = M % 10
    if (a+b) < 10:
        M = 10*b + (a+b)
        count += 1
        if M == N:
            print(count)
            break
    elif (a+b) >= 10:
        M = (10*b + (a+b-10))
        count += 1
        if M == N:
            print(count)
            break



