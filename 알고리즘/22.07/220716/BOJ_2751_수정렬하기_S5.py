
# 이 문제에서는 정수가 음수가 존재할 수 있는 상황
# 하지만 병합정렬에서는 숫자가 음수이면 사용할 수가 없다.
# 음수를 정렬할 때는 어떻게 해야할까?

unsorted_list = []

N = int(input())
for x in range(N):
    unsorted_list.append(int(input()))


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)

    return merge(left1, right1)

def merge(left, right):
    i = 0
    j = 0
    empty_list = []

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            empty_list.append(left[i])
            i += 1

        else:
            empty_list.append(right[j])
            j += 1

    while i < len(left):
        empty_list.append(left[i])
        i += 1

    while j < len(right):
        empty_list.append(right[j])
        j += 1

    return empty_list

answer_list = merge_sort(unsorted_list)

for x in answer_list:
    print(x)


