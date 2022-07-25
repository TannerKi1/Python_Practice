# import time

N, M = list(map(int, input().split()))
list_1 = []
list_2 = []
for _ in range(N):
    list_1.append(input())

for _ in range(M):
    list_2.append(input())

set_1 = set(list_1)
set_2 = set(list_2)

set_3 = set_1 & set_2

answer = list(set_3)
answer.sort()
print(len(answer))
for x in answer:
    print(x)


# 겹치는 걸 구할 땐 list에서 append 보다는 그냥 set으로 교집합 때리는 게 훨씬 더 빠른 시간 복잡도를 보장한다.