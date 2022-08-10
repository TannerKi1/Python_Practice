n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c #노선은 하나가 아닐 수 있다. 어떻게 업데이트 할까? 작은 경우에만 갱신해주면 된다!
    else:
        continue

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('INF', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()