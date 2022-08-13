# 방문할 때 마다 + 1 올려서 최댓값 찾는 프로젝트
from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input()))) #지도 생성 완료

# 개별 격자를 좌표값으로 받아서 queue에 넣어주기

# 4방향 지시표 만들어주기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue # pass랑 continue차이 다시 생각해보기

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]


print(bfs(0, 0))




