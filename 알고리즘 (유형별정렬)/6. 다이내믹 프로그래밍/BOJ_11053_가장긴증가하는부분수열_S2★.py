# 증가하는 걸 카운팅하고 기준 값을 새로고침해주기
import sys
N = int(input()) # 반복해야하는 길이
arr = list(map(int, sys.stdin.readline().split()))

minIndex = 0
count = 0
for i in range(N):
    if arr[i] > minIndex:
        count += 1
        minIndex = arr[i]

print(count)

# 반례


# 30 10 20 50 60 70

# 30 50 60 70 -> 길이 4
# 10 20 50 60 70 -> 길이 5


# 이 문제는 DP를 알아야 풀 수 있는 문제이다. 킵
