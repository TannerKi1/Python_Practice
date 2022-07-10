T = int(input())

computer = [
    [1],
    [2, 4, 8, 6],
    [3, 9, 7, 1],
    [4, 6],
    [5],
    [6],
    [7, 9, 3, 1],
    [8, 4, 2, 6],
    [9, 1],
    [10]
]

for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10
    if a == 1:
        b = b % b
        print(computer[a-1][b-1])
    elif a == 2:
        b = b % 4
        print(computer[a-1][b-1])
    elif a == 3:
        b = b % 4
        print(computer[a-1][b-1])
    elif a == 4:
        b = b % 2
        print(computer[a-1][b-1])
    elif a == 5:
        b = b % b
        print(computer[a-1][b-1])
    elif a == 6:
        b = b % b
        print(computer[a-1][b-1])
    elif a == 7:
        b = b % 4
        print(computer[a-1][b-1])
    elif a == 8:
        b = b % 4
        print(computer[a-1][b-1])
    elif a == 9:
        b = b % 2
        print(computer[a-1][b-1])
    elif a == 0:
        b = b % b
        print(computer[a-1][b-1])




