n = int(input())
d = [0]

d.append(1)
d.append(3)

for i in range(3, n+1):
    d.append(d[i-2] * 2 + d[i-1])

print(d[n])
