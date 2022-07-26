import sys

N = int(input())
arr = []

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
            arr.pop(0)

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

