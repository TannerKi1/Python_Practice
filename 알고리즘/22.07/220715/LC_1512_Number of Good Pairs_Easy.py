

nums = [1, 1, 1, 1]

# 아이디어 i를 시작점에 고정, j를 i+1위치에 놓고 오른쪽으로 한 칸씩 옮기면서 탐색을 한다.
# j가 끝위치에 다다르면, i의 시작점을 오른쪽으로 한칸만 옮긴 후에 다시 해당 액션을 반복 수행한다.

i = 0
j = i+1

count = 0
for i in range(0, len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            count += 1
print(count)


# 돌아는 가는데, 시간 복잡도가 for 2번을 돌린 N**2라서 개선의 여지가 많이 남아있음



