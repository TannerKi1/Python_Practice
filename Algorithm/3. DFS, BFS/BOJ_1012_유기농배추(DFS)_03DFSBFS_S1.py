

# dfs 함수 선언
def dfs(r, c):

    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False

    if grid[r][c] == 1:
        grid[r][c] = 0
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
        return True
    return False


# 테스트 케이스 개수 선언
T = int(input())

# 가로, 세로, 벌레 다운로드
for _ in range(T):
    cols, rows, k = map(int, input().split())

    # 그리드 만들기
    grid = [[0] * cols for _ in range(rows)]

    # 벌레 정보 심기
    for _ in range(k):
        c, r = map(int, input().split())
        grid[r][c] = 1

    # 벌레 카운트하기
    cnt = 0
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c):
                cnt += 1

    print(cnt)




