# 머지소트 매일매일 그냥 쌩으로 써보기!!

list_ = [2, 5, 6, 1, 2, 6, 7, 10, 5]

def merge_sort(list_):
    if len(list_) <= 1:
        return list_

    while len(list_) >= 2:
        mid = len(list_) // 2
        left = list_[:mid]
        right = list_[mid:]

        left_1 = merge_sort(left)
        right_1 = merge_sort(right)
        return merge(left_1, right_1)

def merge(left, right):
    i = 0
    j = 0
    sorted_list = []

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while (i < len(left)):
        sorted_list.append(left[i])
        i += 1

    while (j < len(right)):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

print(merge_sort(list_))





