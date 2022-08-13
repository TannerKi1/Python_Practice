TC = int(input())

d = [1, 1]

for i in range(2, 31):
    d.append(d[i-1] * i)

# 팩토리얼 dp로 구해놨고.

for _ in range(TC):
    M, N = map(int, input().split())
    print(int(d[N]/(d[M]*d[N-M])))

# C 값을 따로 내장함수 안 쓰고 구하고. 함수 불러오면 더 빨리 풀 수도 있을 듯.
