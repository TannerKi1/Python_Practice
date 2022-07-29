import sys
N = int(sys.stdin.readline())
num_list = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    num_list.append([a, b])

A = 0
B = 0
for i in range(N):
    if i <= N-2:
        A += num_list[i][0] * num_list[i+1][1]
        B += num_list[i][1] * num_list[i+1][0]

    elif i == N-1:
        A += num_list[i][0] * num_list[0][1]
        B += num_list[i][1] * num_list[0][0]

print(round(abs(A-B)/2, 1))


