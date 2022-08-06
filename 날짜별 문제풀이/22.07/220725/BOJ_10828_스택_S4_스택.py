import sys

N = int(input())
arr = []
for _ in range(N):
    command = list(sys.stdin.readline().split())
    if len(command) == 2:
        order = command[0]
        number = int(command[1])

    else:
        order = command[0]

    if order == 'push':
        arr.append(number)

    elif order == 'top':
        if len(arr) >= 1:
            print(arr[-1])
        else:
            print(-1)

    elif order == 'size':
        print(len(arr))

    elif order == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)

    elif order == 'pop':
        if len(arr) >= 1:
            print(arr[-1])
            arr.pop(-1)

        else:
            print(-1)

