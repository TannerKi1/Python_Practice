import sys
from collections import deque
input = sys.stdin.readline

# 나이트가 가능한 이동방향 좌표 정리
dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]


# bfs함수 정의, 시작점x, 시작점y, 끝점x, 끝점y를 x, y, a, b로 정의함
def bfs(x, y, a, b):

    queue = deque()
    queue.append((x, y))

    while queue:
        kx, ky = queue.popleft()

        if kx == a and ky == b:
            print(graph[kx][ky] - 1)

        for i in range(8):
            nx = kx + dx[i]
            ny = ky + dy[i]

            # 새로 나온 말의 범위가 지도 밖인 경우에는 다른 값으로 돌아감
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 이미 방문한 경우에도 무시함. 넓이 우선 탐색이기 때문에 0이 아니라면 그게 최소 방문 횟수임.
            if graph[nx][ny] != 0:
                continue

            # 지도 안의 범위이고, 한번도 방문하지 않았다면, 직전에 방문했던 횟수에서 1을 더해준다.
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[kx][ky] + 1
                queue.append((nx, ny))


# 테스트 케이스 가지수 입력
T = int(input())


for _ in range(T):
    n = int(input())
    graph = [[0] * n for _ in range(n)]

    x, y = map(int, input().split())
    a, b = map(int, input().split())
    graph[x][y] = 1
    bfs(x, y, a, b)

