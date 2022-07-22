N = int(input())

sugar = [3, 5]
d = [10001] * 5001
d[0] = 0
for i in range(len(sugar)):
    for j in range(2, N+1):
        if d[j - sugar[i]] != 10001:
            d[j] = min(d[j], d[j - sugar[i]] + 1)


if d[N] == 10001:
    print(-1)
else:
    print(d[N])


# DBB 226이랑 같은 원리임