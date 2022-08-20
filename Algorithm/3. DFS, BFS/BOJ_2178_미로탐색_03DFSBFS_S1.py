from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                queue.append((nx, ny))


bfs(0, 0)
print(graph[n-1][m-1])