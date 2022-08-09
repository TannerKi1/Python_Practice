import time

n = int(input())
item = list(map(int, input().split()))

m = int(input())
order = list(map(int, input().split()))

# start = time.time()
# for x in order:
#     if x in item:
#         print('yes')
#     else:
#         print('no')
#
# print(time.time() - start)

### 이진탐색으로 푸는 법

item.sort()

start = 0
end = len(item)

def binary_search(start, end, target, arr):
    start = 0
    end = len(item)


    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return True

        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

    return False


for x in order:
    if binary_search(start, end, x, item):
        print('yes')
    else:
        print('no')






