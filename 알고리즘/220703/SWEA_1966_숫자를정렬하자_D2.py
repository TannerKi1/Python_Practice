
T = int(input())
N = int(input())

for x in range(1, T+1):
    b = list(map(int, input().split()))
    b.sort()

    print(f'#{x}', end=' ')
    for j in range(0, N):
        print(b[j], end=' ')
    print()



# 줄이 다른걸 print()로 마지막에 받으면 한 줄로 합쳐져서 나오나?