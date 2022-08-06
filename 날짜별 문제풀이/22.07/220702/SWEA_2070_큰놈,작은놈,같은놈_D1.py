
# 목표 : 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라

T = int(input())

for i in range(1, T+1):
    b = list(map(int, input().split()))
    if b[0] > b[1]:
        print(f'#{i} >')
    elif b[0] == b[1]:
        print(f'#{i} =')
    elif b[0] < b[1]:
        print(f'#{i} <')


