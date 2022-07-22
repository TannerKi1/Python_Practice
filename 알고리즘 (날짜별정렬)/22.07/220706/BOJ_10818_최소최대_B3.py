# min, max로 하면 쉽겠지만

# 최댓값, 최소값 고르기 연습을 할 수 있음.

# N = int(input())
#
# # N개의 정수가 들어온다.
#
# T = list(map(int, input().split()))
#
# min_Idx = 0
# max_Idx = 0
#
# for i in range(N):
#     if T[min_Idx] <= T[i]:
#         continue
#     elif T[min_Idx] > T[i]:
#         min_Idx = i
#
# for k in range(N):
#     if T[k] >= T[max_Idx]:
#         max_Idx = k
#     elif T[k] < T[max_Idx]:
#         continue
#
# print(T[min_Idx], end=' ')
# print(T[max_Idx])

### 다르게 푸는법

N = int(input())

T = list(map(int, input().split()))
a = min(T)
b = max(T)

print(a, end=' ')
print(b)


