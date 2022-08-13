T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = []

    for _ in range(N):
        graph.append(list(map(int, input().split())))

    for a in range(N):
        for b in range(N):
            if graph[a][b] == 0:
                graph[a][b] = int(1e9) # 연결 없는 값을 무한으로 초기화를 해줘야한다.

    for a in range(N):
        graph[a][a] = 0

    for k in range(N):
        for a in range(N):
            for b in range(N):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    answer = 0

    for a in range(N):
        for b in range(N):
            if graph[a][b] > answer:
                answer = graph[a][b]

    print(f'#{tc} {answer}')