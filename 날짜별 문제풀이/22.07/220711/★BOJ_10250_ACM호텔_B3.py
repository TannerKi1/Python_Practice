T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    floor_room = N % H
    if floor_room == 0:
        end_room = N // H
        floor_room = H
        if end_room < 10:
            print(int(str(floor_room) + '0' + str(end_room)))
        else:
            print(int(str(floor_room) + str(end_room)))
    elif floor_room != 0:
        end_room = N // H + 1
        if end_room < 10:
            print(int(str(floor_room) + '0' + str(end_room)))
        else:
            print(int(str(floor_room) + str(end_room)))

