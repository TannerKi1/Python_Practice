N = int(input())

b = list(map(int, input().split()))
M = max(b)
c = []
for j in range(0, N):
    c.append(b[j]/M*100)

print(sum(c)/N)


