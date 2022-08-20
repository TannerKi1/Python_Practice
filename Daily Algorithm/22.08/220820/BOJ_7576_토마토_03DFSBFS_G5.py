from collections import deque
# bfs의 시작점이 여러개일 경우에는 어떻게 처리할 것인지?
# 동빈북 실전문제 경쟁적전염의 하위호환. 경쟁적 전염은 여기에 시간 티커를 넣으면 완성되는 문제

w, h = map(int, input().split())

# 지도 생성 (성공)
# 우선 썩은 토마토가 있는 위치를 받아오기(성공)

graph = []
virus = []
for i in range(h):
    graph.append(list(map(int, input().split())))
    for j in range(w):
        if graph[i][j] == 1:
            virus.append((i, j))


# 모든 썩은 토마토의 좌표를 덱에 넣어줘야한다. 그래야 가장 먼거리부터 순차적으로 조금씩 감염시킬 수 있음.
# 해당 개념은 경쟁적 전염에서도 똑같이 사용되었던 개념임.
queue = deque()

for item in virus:
    x, y = item
    queue.append((x, y))


while queue:
    a, b = queue.popleft()

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        # 좌표범위 밖이면 돌아가기
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue

        # 벽이면 돌아가기
        if graph[nx][ny] == -1:
            continue

        # 좌표평면 안이고, 벽도 아니면 감염시키기
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[a][b] + 1
            queue.append((nx, ny))


zero_count = 0
max_day = 0
for x in range(h):
    for y in range(w):
        if graph[x][y] >= max_day:
            max_day = graph[x][y]
        if graph[x][y] == 0:
            zero_count += 1

if zero_count == 0:
    print(max_day - 1)
else:
    print(-1)

