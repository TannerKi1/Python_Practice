V = int(input())
E = int(input())
INF = int(1e9)
graph = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, V+1):
    graph[i][i] = 0


for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for i in range(1, V+1):
    for j in range(1, V+1):
        print(graph[i][j], end=' ')
    print()

