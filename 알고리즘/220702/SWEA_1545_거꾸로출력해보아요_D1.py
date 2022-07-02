

N = int(input())

b = []
for x in range(0, N+1):
    b.append(x)

k = sorted(b, key=lambda x : x, reverse = True)

for j in k:
    print(j, end=' ')




