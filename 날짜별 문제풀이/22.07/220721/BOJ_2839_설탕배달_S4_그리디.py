N = int(input())
array = [3, 5]

d = [10001] * N+1

d[0] = 0

for i in range(len(array)):
    for j in range(1, N+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], (d[j - array[i]] + 1))

if d[N] != 10001:
    print(d[N])
else:
    print(-1)



## 바텀업 방식을 잘 기억해놓자