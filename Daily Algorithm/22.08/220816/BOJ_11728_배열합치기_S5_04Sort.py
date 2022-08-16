N, M = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

# 리스트를 어떻게 합치면 좋을까?

arr_3 = arr_1 + arr_2 # 파이썬에서는 +로 된다.

arr_3.sort()

print(*arr_3)
