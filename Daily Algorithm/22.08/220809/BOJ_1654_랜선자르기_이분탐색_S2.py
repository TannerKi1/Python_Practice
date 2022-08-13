n, k = map(int, input().split())
lan = []
for _ in range(n):
    lan.append(int(input()))

start = 1 # 나무자르기일 때는 0이 상관 없었는데... 이게 end 값이 0으로 수렴하는 경우도 나온다는 이야기네.
end = max(lan)

result = 0
while start <= end:
    mid = (start + end) // 2

    count = 0
    for item in lan:
        count += item // mid

    if count < k:
        end = mid - 1

    if count >= k:
        start = mid + 1
        result = mid

print(result)




