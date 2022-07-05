# min, max로 하면 쉽겠지만

# 버블 소팅을 연습해볼 수 있는 문제

N = int(input())

# N개의 정수가 들어온다.

T = list(map(int, input().split()))

min_Idx = 0
max_Idx = 0

for i in range(N):
    if T[min_Idx] <= T[i]:
        continue
    elif T[min_Idx] > T[i]:
        min_Idx = i

for k in range(N):
    if T[k] >= T[max_Idx]:
        max_Idx = k
    elif T[k] < T[max_Idx]:
        continue

print(T[min_Idx], end=' ')
print(T[max_Idx])




