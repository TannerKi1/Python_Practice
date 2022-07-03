
# 카운팅 정렬 연습

arr = [0, 1, 9, 2, 4, 7, 3, 5, 1]

count = [0] * (max(arr) + 1)

for x in arr:
    count[x] += 1

for k in range(1, len(count)):
    count[k] = count[k-1] + count[k]

result = [0] * (len(arr))

print(count)

for num in arr:
    idx = count[num]
    result[idx - 1] = num
    count[num] -= 1
    print(count)
    print(result)


