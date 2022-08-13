import math

M = int(input())
N = int(input())

M_list = []
for i in range(1, M):
    if math.sqrt(i) == int(math.sqrt(i)):
        M_list.append(i)


N_list = []
for i in range(1, N+1):
    if math.sqrt(i) == int(math.sqrt(i)):
        N_list.append(i)

answer = []
for z in N_list:
    if z not in M_list:
        answer.append(z)

if len(answer) >= 1:
    print(sum(answer))
    print(min(answer))

else:
    print(-1)