T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))

    graph = []
    for i in range(0, N*M, M):
        graph.append(array[i:i+M])

    # 그래프 초기화 완료

    for j in range(1, M):
        for i in range(N):
            if i == 0:
                left_up = 0
            else:
                left_up = graph[i - 1][j - 1]

            if i == N-1:
                left_down = 0
            else:
                left_down = graph[i + 1][j - 1]

            left = graph[i][j-1]
            graph[i][j] = graph[i][j] + max(left_down, left_up, left)

    result = 0
    for i in range(N):
        result = max(result, graph[i][M-1])

    print(result)
    print(graph)
