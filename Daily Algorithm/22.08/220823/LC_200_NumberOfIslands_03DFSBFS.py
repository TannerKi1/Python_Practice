from collections import deque

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

rows = len(grid)
cols = len(grid[0])

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        r, c = queue.popleft()

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue

            if grid[nr][nc] == '1':
                grid[nr][nc] = 0
                queue.append((nr, nc))

cnt = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '1':
            grid[r][c] = 0
            bfs(r, c)
            cnt += 1

print(cnt)


























# def dfs(x, y):
#
#     if x < 0 or x >= rows or y < 0 or y >= cols:
#         return False
#
#     if grid[x][y] == '1':
#         grid[x][y] = 0
#         dfs(x - 1, y)
#         dfs(x + 1, y)
#         dfs(x, y - 1)
#         dfs(x, y + 1)
#         return True
#     return False
#
#
# cnt = 0
# for r in range(rows):
#     for c in range(cols):
#         if dfs(r, c):
#             cnt += 1
#
# print(cnt)

