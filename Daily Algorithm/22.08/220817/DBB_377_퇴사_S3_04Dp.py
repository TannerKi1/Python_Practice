N = int(input())
T = []
P = []
d = [0] * (N + 1)
max_value = 0
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N-1, -1, -1):
    time = T[i] + i
    if T[i] + i <= N:
        d[i] = max(P[i] + d[time], max_value)
        max_value = d[i]

    else:
        d[i] = max_value

print(max(d))

