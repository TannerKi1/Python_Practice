# 사용가능한 이진수

n = int(input())

d = []

d.append(0)
d.append(1)
d.append(2)

if n <= 2:
    print(d[n] % 15746)
    exit() # 이거 안하면 2 이하일 때 값이 2번 나오게 된다.

if n >= 3:
    for n in range(3, n+1):
        d.append((d[n-1] + d[n-2]) % 15746)

print(d[n])