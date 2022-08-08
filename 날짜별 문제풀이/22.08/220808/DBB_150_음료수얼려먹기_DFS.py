#2회차 풀이

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False


cnt = 0


for x in range(n):
    for y in range(m):
        if dfs(x, y):
            cnt += 1

print(cnt)
