from bisect import bisect_left

# 6
# 4 2 6 3 1 5

n = int(input())
array = list(map(int, input().split()))

answer = []
for num in array:
    if bisect_left(answer, num) == len(answer):
        answer.append(num)
    else:
        answer[bisect_left(answer, num)] = num

print(len(answer))
