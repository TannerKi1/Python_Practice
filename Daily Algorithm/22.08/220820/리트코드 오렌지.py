from collections import deque

grid = [[0,2]]

n = len(grid)
m = len(grid[0])

virus = []

no_orange = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            virus.append((i, j))
        if grid[i][j] == 1:
            no_orange += 1


queue = deque()

for i in virus:
    x, y = i
    queue.append((x, y))

while queue:
    a, b = queue.popleft()

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if grid[nx][ny] == 0:
            continue

        if grid[nx][ny] == 1:
            grid[nx][ny] = grid[a][b] + 1
            queue.append((nx, ny))

zero_count = 0
max_value = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] >= max_value:
            max_value = grid[i][j]
        if grid[i][j] == 1:
            zero_count += 1


if no_orange == 0: # 처음부터 신선한 오렌지가 없었다면...?
    print(0)

else: #처음부터 신선한 오렌지는 있었으나
    if zero_count >= 1: # 벽으로 인해 오염되지 않은 오렌지가 있다면
        print(-1)
    else: # 그게 아니라 모두 오염되었다면.
        print(max_value - 2)








