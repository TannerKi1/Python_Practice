T = int(input())

for tc in range(1, T+1):
    n, a, b = map(int, input().split())

    arr = [[1], [1, 1]]

    for i in range(2, n+1):
        t = [1]
        for j in range(1, i):
            t.append(arr[i-1][j-1] + arr[i-1][j])
        t.append(1)
        arr.append(t)

    print(f'#{tc} {arr[n][b]}')

# 파스칼 삼각형 빠르게 만드는 DP는 외워둘 것