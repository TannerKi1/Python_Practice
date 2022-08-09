n, k = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

while start <= end:

    mid = (start + end) // 2

    total = 0
    for tree in arr:
        if tree > mid :
            total += tree - mid

    if total < k:
        end = mid - 1  # 왜 모자라면 end값을 줄어져줘야하는지 생각해보기

    else:
        result = mid
        start = mid + 1

print(result)





