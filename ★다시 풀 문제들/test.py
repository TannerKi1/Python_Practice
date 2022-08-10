# 다익스트라 버전2.0
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
start = int(input())

graph = [ [] for _ in range(V+1)]
# visited = [False] * (V + 1)
distance = [INF] * (V + 1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 준비완료

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

dijkstra(start)

for i in range(1, V+1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print("INFINITE")




