import sys
N = int(input())
sort_arr = list(map(int, sys.stdin.readline().split()))
M = int(input())
target_arr = list(map(int, sys.stdin.readline().split()))


sort_arr.sort()

for x in target_arr:
    left = 0
    right = len(sort_arr) - 1
    isExist = False # 스위치로 처리하는 방법.

    while left <= right:
        mid = (left + right) // 2

        if x == sort_arr[mid]:
            isExist = True
            print(1)



        elif x < sort_arr[mid]:
            right = mid - 1

        elif x > sort_arr[mid]:
            left = mid + 1

    if not isExist:
        print(0)
