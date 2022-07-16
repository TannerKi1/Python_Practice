# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
nums = [3, 2, 4]
target = 6

# sol(1) 가장 쉬운 방법은 역시 Brute Force로 일일이 대입하는 것
# # 하지만 for문을 2번 돌렸기 때문에 시간 복잡도는 n**2로 측정된다.
# # 더 효율적인 풀이가 아래에 있다.
#
#         for x in range(len(nums)):
#             for y in range(x + 1, len(nums)):
#                 if nums[x] + nums[y] == target:
#                     return [x, y]

# sol(2) 만약 오름차순으로 리스트가 주어진다면, 혹은 target과 일치하는 count 헤아릴 때는 활용가능함. 하지만 이번 문제에서는 활용 불가능함
# sorted_nums = [3, 2, 4]
# target = 6
#
# 우선 오름차순으로 소팅을 해준다.
#
# 다음에 i 값을 0, j 값은 len(sorted_nums) - 1로 해준다.
#
# i = 0
# j = len(sorted_nums) - 1
#
# while i < j:
#     if sorted_nums[i] + sorted_nums[j] > target: # 타겟보다 크면
#         j -= 1 # j티커를 왼쪽으로 한칸씩 옮겨 두 개의 합을 낮춰준다.
#
#     elif sorted_nums[i] + sorted_nums[j] < target : # 타겟보다 작으면
#         i += 1 # i티커를 오른쪽으로 한칸씩 옮겨 두 개의 합을 높여준다.
#
#     elif sorted_nums[i] + sorted_nums[j] == target : # 만약 타겟과 일치하면
#         print([i, j]) #i 값과 j값을 리턴
#         break
#
# 그런데 이 방법은 정확히 똑같이 일치하는 인덱스를 출력해야하는 이 문제에서는 사용할 수 없다.

# sol(3)
# 우수 답안은 '해시 테이블'을 우수 풀이로 제시하고 있다. 자료구조 (6)에 해당하는 것으로 반드시 알아야하는 개념이다.
# 공간 복잡도를 희생하고, 시간 복잡도를 챙기는 방법으로서, 값을 해시 맵에 저장해서 찾으면 가져오는 개념으로 파악된다.

hashmap = {} # 딕셔너리 값을 쓰겠다. key와 value를 가지는
for i in range(len(nums)): # 0, 1, 2 카운팅
    hashmap[nums[i]] = i # 3: 0, 2: 1, 4: 2 로 맵에 들어가게 된다.
for i in range(len(nums)):
    complement = target - nums[i]
    # 3, 4, 2 순으로 나오게 된다.
    if complement in hashmap and hashmap[complement] != i:  #뒤의 조건은 자신과 동일한 값을 리턴하는 걸 방지
        print ([i, hashmap[complement]])

print(hashmap)
print(hashmap[4])
# Brute Force로 for문 2번 돌렸을 때 시간 복잡도는 O(n**2), 24% 대비 우수도 리턴됨

# Hashmap으로 리턴하면 시간복잡도는 O(n), 56% 대비 우수도

