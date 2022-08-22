

# dfs 함수 선언
def dfs(c, r):

    if c < 0 or c >= cols or r < 0 or r >= rows:
        return False

    if grid[c][r] == 1:
        grid[c][r] = 0
        dfs(c - 1, r)
        dfs(c + 1, r)
        dfs(r, c - 1)
        dfs(r, c + 1)
        return True
    return False


# 테스트 케이스 개수 선언
T = int(input())

# 가로, 세로, 벌레 다운로드
for _ in range(T):
    rows, cols, k = map(int, input().split())

    # 그리드 만들기
    grid = [[0] * rows for _ in range(cols)]

    # 벌레 정보 심기
    for _ in range(k):
        r, c = map(int, input().split())
        grid[c][r] = 1

    cnt = 0
    for c in range(cols):
        for r in range(rows):
            if dfs(c, r):
                cnt += 1

    print(cnt)




