
T = int(input())

for i in range (1, T+1):
    a = list(map(int, input().split()))

    print(f'#{i} {round(sum(a)/10)}')


# round() 함수 사용법 익히기