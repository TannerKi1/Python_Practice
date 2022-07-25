# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
#
# empty_arr1 = []
# target = 0
# for i in range(1 << N):
#     empty_arr = []
#     for j in range(N):
#         if i & (1 << j):
#             empty_arr.append(arr[j])
#
#     if len(empty_arr) == 3:
#         if sum(empty_arr) < M:
#             target = max(target, sum(empty_arr))
#
#         elif sum(empty_arr) == M:
#             print(sum(empty_arr))
#             exit()
#
# else:
#     print(target)

## 시간 초과. 부분집합 3개짜리 구하는 게 시간을 많이 먹는 듯 하다.

# 3중 포문을 돌려야하나?

print(100**3)






