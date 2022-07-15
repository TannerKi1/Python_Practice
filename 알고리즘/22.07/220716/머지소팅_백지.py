unsorted_list = [1, 2, 7, 7, 1]

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
    answer_list = []

    i = 0
    j = 0

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            answer_list.append(left[i])
            i += 1

        else:
            answer_list.append(right[j])
            j += 1

    while i < len(left):
        answer_list.append(left[i])
        i += 1

    while j < len(right):
        answer_list.append(right[j])
        j += 1

    return answer_list

print(merge_sort(unsorted_list))
