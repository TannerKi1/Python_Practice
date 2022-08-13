'''
from bisect import bisect_left

N = int(input())
array = list(map(int, input().split()))


def bisect_checker(array):
    for x in array:
        if x != bisect_left(array, x):
            continue
        else:
            return x

    else:
        return -1

print(bisect_checker(array))
'''
## 이 방법은 선형 탐색이기 때문에 시간 초과가 났을 것이다.

N = int(input())
array = list(map(int, input().split()))



def checker(array):
    start = 0
    end = len(array)

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid

        elif array[mid] > mid:  # 버리는 거 잘 캐치하기
            end = mid - 1

        elif array[mid] < mid:
            start = mid + 1

    return -1

print(checker(array))
