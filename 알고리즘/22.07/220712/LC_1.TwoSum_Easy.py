#
#
# # 하지만 for문을 2번 돌렸기 때문에 시간 복잡도는 n**2로 측정된다.
# # 더 효율적인 풀이가 아래에 있다.
#
#         for x in range(len(nums)):
#             for y in range(x + 1, len(nums)):
#                 if nums[x] + nums[y] == target:
#                     return [x, y]