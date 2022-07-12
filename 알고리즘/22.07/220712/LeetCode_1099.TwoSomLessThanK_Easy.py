# Input: nums = [34,23,1,24,75,33,54,8], k = 60
# Output: 58
# Explanation: We can use 34 and 24 to sum 58 which is less than 60.

nums = [34,23,1,24,75,33,54,8]
k = 60

sort_x = []
sort_y = []
sort_sum = []

    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] < k:
            sort_x.append(nums[x])
            sort_y.append(nums[y])
            sort_sum.append(nums[x] + nums[y])

    if len(sort_sum) != 0:
        answer3 = max(sort_sum)


    elif len(sort_sum) == 0:
        print( -1)

#####위에 방법이 가장 무식한 방법. 그냥 모든 숫자를 더해서 비교해보는 방식이고,
# 훨씬 효율성이 더 높은 풀이가 아래에 등장함.
# 투포인터 같은데.. 오름차순으로 정렬된 값이 있을때, 왼쪽에서는 올라갈수록 값이 커지고, 오른쪽에서 한칸 빠지면 값이 작아지는 원리를 이용한 방식
# [1, 2, 3, 4, 5] 에서 7보다 큰 값을 찾아간다고 가정해보자.
# i와 j가 있다면 i는 가장 작은 값인 0을 가지고, j는 가장 큰 값인 len(ex)-1이다. 인덱스 값이기 때문에 j가 4여야지 ex[4] == 5로 인식된다.
1 + 5 = 6 작기 때문에 왼쪽티커를 하나 올려서 2 + 5를 검사해본다. 여전히 작기 때문에 하나 더 올린다 ... 그러면 4 + 5에서 걸린다.


class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxSum = -1
        i = 0
        j = len(nums) - 1

        nums.sort()

        while i < j:
            if nums[i] + nums[j] < k:
                maxSum = max(maxSum, nums[i] + nums[j])
                i += 1
            else:
                j -= 1
        return maxSum


