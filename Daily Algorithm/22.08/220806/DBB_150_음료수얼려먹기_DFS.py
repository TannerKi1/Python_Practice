n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= - 1 or x >= n or y <= - 1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True # 한 번 돌 때 채울 수 있는 건 다 채웠기 때문에 인접한 0들은 False로 처리되게 됨.
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            print(i, j)
            result += 1


