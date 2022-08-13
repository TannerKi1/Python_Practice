d = [0]

d.append(1)
n = int(input())

if n == 0:
    print(0)
    exit()

if n == 1:
    print(0)
    exit()

if n >= 2:
    for x in range(2, n+1):
        d.append(x * d[x-1])


count = 0
for k in str(d[n])[::-1]:
    if k == '0':
        count += 1
    else:
        break

print(count)

# 재귀로 팩토리얼 계산하려하면 난리남. DP에 저장해서 불러오는 게 훨씬 더 효율적인 방법임

