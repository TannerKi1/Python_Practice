from collections import deque

n, m = map(int, input().split())

graph = []
# 그래프 생성 완료
for _ in range(n):
    graph.append(list(map(int, input())))


# # dfs 함수
# def dfs(x, y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return False
#
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x - 1, y)
#         dfs(x + 1, y)
#         dfs(x, y - 1)
#         dfs(x, y + 1)
#         return None
#     return False
#
# # 실제 함수 실행
# cnt = 0
#
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) is None:
#             cnt += 1
#
# print(cnt)

def bfs(a, b):

    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # if graph[nx][ny] != 0:
            #     continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))


cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            graph[i][j] = 1
            bfs(i, j)
            cnt += 1

print(cnt)