T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    result = []

    arr = []
    for _ in range(N):
        arr.append(input())

    # 가로검색

    for r in range(N): # 20
        for c in range(N - M + 1): # 13 ... range(8) # 시작점을 이렇게 잡아 준다.
            if arr[r][c: c+M] == arr[r][c: c+M][::-1]:
                result.append(arr[r][c: c+M])

    # 세로검색

    for r in range(N - M + 1):
        for c in range(N):
            c_list = []
            for i in range(M):
                c_list.append(arr[r+i][c])

    # 세로 검색 코드가 좀 가로에 비해 직관적이지 않은데, 세로 코드를 직관적으로 짜보는 건...?






