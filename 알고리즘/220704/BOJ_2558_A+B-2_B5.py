import sys
N = 2
lines = sys.stdin.readline()
b = []

for lines in range(1, N+1):
    b.append(int(lines))
print(sum(b))
