# 찾고자 하는 어떤 숫자가 list에 있는지 확인하기 위해서는 이진탐색... is in 을 사용할 수도 있겠지만,
# 함수가 금지되어 있다면 어떻게 찾을 것인지 고민은 해야함.

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))


# 딕셔너리로는 한계가 있다. 이진탐색을 활용해보자

arr1.sort()

def binary_search(array, target, left, right):
    while left <= right:
        mid = (left+right) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            right = mid - 1

        elif array[mid] < target:
            left = mid + 1
    return False

for i in range(M): # M번 반복할 거다 아니면 len(arr2)로 해도 가능은 할 듯.
    if binary_search(arr1, arr2[i], 0, N-1) is not False:
        print(1, end=' ')
    else:
        print(0, end=' ')




