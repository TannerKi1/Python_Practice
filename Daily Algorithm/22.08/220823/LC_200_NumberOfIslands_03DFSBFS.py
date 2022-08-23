grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

rows = len(grid)
cols = len(grid[0])


def dfs(x, y):

    if x < 0 or x >= rows or y < 0 or y >= cols:
        return False

    if grid[x][y] == '1':
        grid[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


cnt = 0
for r in range(rows):
    for c in range(cols):
        if dfs(r, c):
            cnt += 1

print(cnt)

