# 목표 주어진 숫자를 소인수 분해해서
# 2, 3, 5, 7, 11 중 몇 개로 이루어진지 찾는 것

T = int(input())

for i in range(1, T+1):
    N = int(input())
    count_11 = 0
    count_7 = 0
    count_5 = 0
    count_3 = 0
    count_2 = 0

    while N > 1:
        if N % 11 == 0:
            count_11 += 1
            N = N // 11
        elif N % 11 != 0:
            if N % 7 == 0:
                count_7 += 1
                N = N // 7
            elif N % 7 != 0:
                if N % 5 == 0:
                    count_5 += 1
                    N = N // 5
                elif N % 5 != 0:
                    if N % 3 == 0:
                        count_3 += 1
                        N = N // 3
                    elif N % 3 != 0:
                        if N % 2 == 0:
                            count_2 += 1
                            N = N // 2
                        elif N % 2 != 0:
                            print("범위초과")
                            break

    while N == 1:
        break

    print(f'#{i} {count_2} {count_3} {count_5} {count_7} {count_11}')