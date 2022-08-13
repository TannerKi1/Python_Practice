
V, E = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for i in range(1, V + 1):
    graph[i][i] = 0

for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


distance = graph[1][K] + graph[K][X]

if distance < INF:
    print(distance)

else:
    print(-1)