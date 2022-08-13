# 백준 나뭇가지 커팅이랑 동일함.

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid: # 더 튀어나온 부분만 total에 합지므로
            total += x - mid

    if total < m:
        end = mid -1


    else: # 떡이 남아도는 경우, 낭비를 줄여야하므로 왼쪽시작점을 중간값 바로 오른쪽으로 이동
        result = mid
        start = mid + 1

print(result)

