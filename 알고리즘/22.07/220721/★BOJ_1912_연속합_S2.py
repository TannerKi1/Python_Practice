# 연속해서 나온 합을 max라는 리스트 합에 저장한다?
import sys
N = int(input())

# list_ = list(map(int, sys.stdin.readline().split()))
#
# max_num = []
#
# for i in range(N):
#     for j in range(i+1, N):
#         a = sum(list_[i:j])
#         if len(max_num) <= 0:
#             max_num.append(a)
#         if len(max_num) >= 1:
#             if a > max(max_num):
#                 max_num.append(a)
#             else:
#                 continue
#
# print(max(max_num))

#### 이렇게 짜면 시간초과가 뜨게 된다. 모든 값 하나하나를 다 대입해줘야하기 때문. for 문 2번이니 N**2
# 전혀 DP스럽지 않은 풀이

arr = [0] + list(map(int, sys.stdin.readline().split()))
cache = [-1001] * (N+1)

for n in range(1, N+1):
    cache[n] = max(arr[n], cache[n-1] + arr[n]) # 총합이 음수면 끊기고 다시 양수버전에서 시작하게 된다.
    
print(max(cache))
