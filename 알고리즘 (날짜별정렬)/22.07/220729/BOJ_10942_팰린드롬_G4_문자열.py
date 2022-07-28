import sys
N = int(sys.stdin.readline())

dp = [[False] * N for _ in range(N)]

arr = list(map(int, sys.stdin.readline().split()))

for idx in range(N):
    for start in range(N):
        end = start + idx
        if end >= N:
            break

        if idx == 0: # 길이가 0, 즉 start값과 end값이 무조건 같으므로
            dp[start][end] = True
            continue # 이게 없으면 끝나버리나?

        if idx == 1: # 길이가 1, 즉 2개의 문자로 되어 있으면...
            if arr[start] == arr[end]:
                dp[start][end] = True
                continue

        if arr[start] == arr[end] and dp[start+1][end-1] == True:
            dp[start][end] = 1 # dp[start+1][end-1]이 먼저 채워진다는 전제가 있다. n * n 그려서 어떤 순서로 채워지는 지 체크


T = int(sys.stdin.readline())

for tc in range(T):
    i, j = map(int, sys.stdin.readline().split())
    if dp[i-1][j-1] == True:
        print(1)
    else:
        print(0)









