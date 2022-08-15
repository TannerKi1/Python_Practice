n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

import heapq

INF = int(1e9)

distance = [INF] * (n + 1)

start = s

graph = [[] for _ in range(n+1)]

for item in fares:
    graph[item[0]].append((item[1], item[2]))
    graph[item[1]].append((item[0], item[2]))

point = []

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        point. append(now)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))



dijkstra(s)

print(distance[1:])

print(distance[a])  # 4에서 출발 6으로
print(distance[b])  # 4에서 출발 2로

print(point)
