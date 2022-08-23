
# 가로세로 정보 다운로드
n = int(input())
rows = n
cols = n

# 그리드 생성
grid = []

# 세로 길이 rows만큼 그리드 정보 다운로드
for _ in range(rows):
    grid.append(list(map(int, input())))

# house 변수 선언
house = 0


# dfs 구현
def dfs(r, c):

    # 함수 외부의 전역변수이기 때문에 global로 선언
    global house

    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False

    if grid[r][c] == 1:
        grid[r][c] = 0
        house += 1
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
        return True
    return False


# 전체 집이 감염되는 횟수 선언
cnt = 0
houses = []
for r in range(rows):
    for c in range(cols):
        if dfs(r, c):
            houses.append(house)
            cnt += 1
            # true가 한번 돌 때 인접한 집은 모두 감염되었기 때문에 다음 집을 위해서 다시 0으로 선언해줘야함.
            house = 0

# 오름차순으로 정렬
houses.sort()

# 전체 횟수와 각각 낮은 숫자부터 인쇄
print(cnt)
for i in range(cnt):
    print(houses[i])



