# bfs를 풀기위한 덱 import
from collections import deque
n, k = map(int, input().split())

# 전체 맵 상황을 담을 판 만들기
grid = []

# 바이러스 각각의 위치 기록과 동시에 덱에 넣기
virus = []
for r in range(n):
    grid.append(list(map(int, input().split())))
    for c in range(n):
        if grid[r][c] != 0:
            virus.append((grid[r][c], r, c, 0))

# (중요) 바이러스의 번호가 낮은 순서대로 증식을 한다.
virus.sort()

# n초뒤, 계산해야하는 x좌표 y좌표 받아놓기
limit, s_x, s_y = map(int, input().split())

# 덱 생성, 안에는 바이러스 값을 넣어줌. 리스트 통채로 넣어줄 수 있다는 사실을 기억할 것.
queue = deque(virus)

while queue:
    name, r, c, second = queue.popleft()

    if second == limit:
        break

    else:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            xx = r + dx[i]
            yy = c + dy[i]

            if xx < 0 or xx >= n or yy < 0 or yy >= n:
                continue

            if grid[xx][yy] != 0:
                continue

            if grid[xx][yy] == 0:
                grid[xx][yy] = name
                queue.append((name, xx, yy, second + 1))

# 결과값 인쇄하기
print(grid[s_x - 1][s_y - 1])