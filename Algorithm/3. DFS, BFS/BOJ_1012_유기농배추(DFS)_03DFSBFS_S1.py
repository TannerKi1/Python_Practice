import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
from collections import deque

# dfs 함수 만들기
def dfs(x, y):

    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 2 # 이걸해야 다른 좌표값이 True나오는 걸 막을 수 있음.
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))




# 테스트 케이스 돌리기
T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    # 가로길이가 m, 세로길이가 n 인 상황

    # 그래프 그리기 완성
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    # # dfs 돌려보기
    # for i in range(n):
    #     for j in range(m):
    #         if dfs(i, j):
    #             cnt += 1

    # print(cnt)
    cnt = 0
    # bfs 돌려보기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                graph[i][j] = 0
                bfs(i, j)
                cnt += 1
    print(cnt)






