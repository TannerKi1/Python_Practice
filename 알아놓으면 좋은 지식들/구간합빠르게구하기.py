
# 동빈북 482페이지 참고

n = 10
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_value = 0
prefix_sum = [0]
for value in data:
    sum_value = sum_value + value
    prefix_sum.append(sum_value)

print(prefix_sum)

# 구간합 계산
for k in range(1, 9):
    left = k
    right = k+2

    print(prefix_sum[right]-prefix_sum[left-1])