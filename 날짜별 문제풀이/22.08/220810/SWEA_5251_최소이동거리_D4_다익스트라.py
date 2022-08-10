import heapq

T = int(input())
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for j in graph[now]:
            cost = dist + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


for tc in range(1, T+1):
    N, E = map(int, input().split())

    distance = [INF] * (N +1)
    graph = [[] for _ in range(N +1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    dijkstra(0)

    print(f'#{tc} {distance[-1]}')




