V, M = map(int, input().split())
INF = int(1e9)

graph = [[INF] *(V+1) for _ in range(V+1)]

for i in range(1, V+1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = 0
for i in range(1, V+1):
    cnt = 0
    for j in range(1, V+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == V:
        result += 1

print(result)

for x in range(1, V+1):
    for y in range(1, V+1):
        print(graph[x][y], end= ' ')
    print()
