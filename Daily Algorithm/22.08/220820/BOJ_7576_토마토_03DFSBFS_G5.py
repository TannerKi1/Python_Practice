from collections import deque
# bfs의 시작점이 여러 개일 경우에는 어떻게 처리할 것인지?
# 동빈북 실전문제 경쟁적전염의 하위호환. 경쟁적 전염은 여기에 시간 티커를 넣으면 완성되는 문제

cols, rows = map(int, input().split())


# 우선 썩은 토마토가 있을 위치를 넣어주기. 어차피 나중에 여기에서 시작하기 때문에 처음부터 덱으로 넣어주는 것이 깔끔함
rotten = deque()

# 지도를 생성하면서 동시에 썩은 토마토의 위치도 갱신
grid = []

# 처음에 싱싱한 토마토 개수 카운트
fresh_cnt = 0

for r in range(rows):
    grid.append(list(map(int, input().split())))
    for c in range(cols):
        if grid[r][c] == 1:
            rotten.append((r, c))
        elif grid[r][c] == 0:
            fresh_cnt += 1


# BFS 시작
while rotten:

    x, y = rotten.popleft()

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        # 좌표범위 밖이면 돌아가기
        if xx < 0 or xx >= rows or yy < 0 or yy >= cols:
            continue

        # 벽이면 돌아가기
        if grid[xx][yy] == -1:
            continue

        # 좌표평면 안의 범위이고, 벽도 아니면 감염시키기
        if grid[xx][yy] == 0:
            # 토마토 상태 갱신해주기
            grid[xx][yy] = grid[x][y] + 1
            # 썩은 토마토에 상태 추가해주기
            rotten.append((xx, yy))
            # 싱싱한 토마토 개수 빼주기
            fresh_cnt -= 1

print(grid)


