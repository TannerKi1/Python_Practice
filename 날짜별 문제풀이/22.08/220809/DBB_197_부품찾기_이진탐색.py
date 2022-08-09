def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1 # -1 로 두었기 때문에 end 값이 start보다 작아지면서 탈출을 할 수 있게 됨

        else:
            start = mid + 1

    return None # while문을 다 돌았는데도 없으면 이 되려면 여기 위치에 indent가 있어야함.


n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
item = list(map(int, input().split()))

for i in item:
    result = binary_search(array, i, 0, n-1)
    if result is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

