from collections import deque
T = int(input())


for tc in range(1, T+1):
    graph = []
    N = int(input())
    for _ in range(N):
        graph.append(list(map(int, input())))
    # 그래프 생성 완료

    # 시작점, 끝점 좌표 평면 받아오기
    basket = []

    for m in range(N):
        for n in range(N):
            if graph[m][n] == 2:
                basket.append((m, n))
                graph[m][n] = 0

    for m in range(N):
        for n in range(N):
            if graph[m][n] == 3:
                basket.append((m, n))
                graph[m][n] = 0

    # 통로랑 벽 체인지

    for m in range(N):
        for n in range(N):
            if graph[m][n] == 1:
                graph[m][n] = 99

    for m in range(N):
        for n in range(N):
            if graph[m][n] == 0:
                graph[m][n] = 1

    def bfs(x, y):

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]


        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                if graph[nx][ny] == 99:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

        return graph[basket[1][0]][basket[1][1]]

    if bfs(basket[0][0], basket[0][1]) == 1:
        print(f'#{tc} {0}')

    else:
        print(f'#{tc} {bfs(basket[0][0], basket[0][1]) - 2}')
