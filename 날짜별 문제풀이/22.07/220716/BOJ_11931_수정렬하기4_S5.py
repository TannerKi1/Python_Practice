import sys
N = int(input())
unsorted_list = []

for _ in range(N):
    a = int(sys.stdin.readline().strip())
    unsorted_list.append(a)

#### 여기까지 리스트 받아왔고 ####

# 근데 int값으로 변환해서 받아왔어야함. str으로 저장된 숫자들은 당연히 정렬이 안됨.
# 숫자같아 보이는 문자열의  대소를 판단할 순 없기 때문에.

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1 :
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
    empty_array = []

    while (i < len(left)) & (j < len(right)):
        if left[i] > right[j]:
            empty_array.append(left[i])
            i += 1

        else:
            empty_array.append(right[j])
            j += 1

    while i < len(left):
        empty_array.append(left[i])
        i += 1

    while j < len(right):
        empty_array.append(right[j])
        j += 1

    return empty_array

answer_list = merge_sort(unsorted_list)

for x in answer_list:
    print(x)


### 아니면 그냥 sorted(unsorted_list, reverse = True)로 처리하는 방법도 있다. 사실 이게 더 간단하지