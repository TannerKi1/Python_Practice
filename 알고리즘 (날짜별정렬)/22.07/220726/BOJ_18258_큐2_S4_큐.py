import sys
from collections import deque

N = int(input())
arr = deque([]) # 왼쪽에서 빼는 경우 시간 복잡도 O(N)이 나오게 된다.  deque를 무조건 쓰자. 왼쪽에서 빼야하는 경우는!

for _ in range(N):
    order_list = list(sys.stdin.readline().split())
    if len(order_list) >= 2 :
        order = order_list[0]
        number = int(order_list[1])

    else:
        order = order_list[0]

    if order == 'push':
        arr.append(number)

    elif order == 'pop':
        if len(arr) >= 1:
            print(arr[0])
            arr.popleft()

        else:
            print(-1)

    elif order == 'size':
        print(len(arr))

    elif order == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)

    elif order == 'front':
        if len(arr) >= 1:
            print(arr[0])
        else:
            print(-1)

    elif order == 'back':
        if len(arr) >= 1:
            print(arr[-1])
        else:
            print(-1)






# n = int(input())
# queue = []
#
# if n == 0:
#     exit()
#
# for tc in range(n):
#     order_list = list(input())
#
#     if len(order_list) >= 2:
#         order = order_list[0]
#         number = int(order_list[1])
#
#     else:
#         order = order_list[0]
#
#     if order == 'push':
#         queue.append(number)
#
#     elif order == 'front':
#         print(queue[0])
#
#     elif order == 'back':
#         print(queue[-1])
#
#     elif order == 'size':
#         print(len(queue))
#
#     elif order == 'empty':
#         if len(queue) == 0:
#             print(1)
#
#         else:
#             print(0)
#
#     elif order == 'pop':
#         if len(queue) >= 1:
#             print(queue[0])
#             queue.pop(0)
#         else:
#             print(-1)
