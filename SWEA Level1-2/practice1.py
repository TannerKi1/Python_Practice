
T = int(input())

for i in range(1, T+1):
    maxIdx = 0
    N = int(input())
    a = list(map(int, input().split()))

    for j in range(0, N):
        if a[maxIdx] < a[j]:
            maxIdx = j


    print(f'#{i} {a[maxIdx]}')
