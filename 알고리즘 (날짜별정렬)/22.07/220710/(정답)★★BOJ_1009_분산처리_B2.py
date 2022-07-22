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


# 일단 a는 뒷자리만 받으면 되니 % 10 처리해주면 되고
# b는 반복 규칙이 있으니, a인 경우에 따라 미리 나눠서 4로 나눈 나머지로 2차원 배열 찾기

