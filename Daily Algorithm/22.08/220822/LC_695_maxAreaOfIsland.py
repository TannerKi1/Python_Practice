grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

rows = len(grid)
cols = len(grid[0])
island = 0


# dfs
def dfs(r, c):
    global island
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
        return False

    if grid[r][c] == 1:
        grid[r][c] = 0
        island += 1
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        return True
    return False


# count island
islands = []
cnt = 0
for r in range(rows):
    for c in range(cols):
        if dfs(r, c):
            cnt += 1
            islands.append(island)
            island = 0

print(max(islands))