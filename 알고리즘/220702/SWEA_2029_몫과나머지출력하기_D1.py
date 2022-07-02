
T = int(input())

for i in range(1, T+1):
    b = list(map(int, input().split()))
    j = b[0]
    k = b[1]
    print(f'#{i} {j//k} {j%k}')
