n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i]) # 이걸 털고, 전에 누적을 받느냐, 아님 안 털고, 바로 직전까지 먹은 게 낫냐를 비교

print(d[n-1])
