nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# # nums = [5,4,-1,7,8]
# nums = [-2,-1]

k = len(nums)

arr = [0] + nums

max_num = [-9999] * (k + 1)


for i in range(1, k+1):
    max_num[i] = max(arr[i], max_num[i-1] + arr[i])

print(max_num)

# dp에서는 max를 진짜진짜 잘쓰자...