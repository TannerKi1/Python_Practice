N = int(input())
M = int(input())
INF = int(1e9)

graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b, cost = map(int, input().split())
    if cost < graph[a][b]: # 이 문제의 핵심. 새로 들어온 노선의 값이 기존의 값보다 저렴할 때만 그래프 가격을 업데이트 시켜준다.
        graph[a][b] = cost

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        print(graph[a][b], end=' ')
    print()