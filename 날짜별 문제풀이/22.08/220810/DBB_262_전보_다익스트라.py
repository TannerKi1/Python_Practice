import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [ [] for _ in range(n+1)]

time = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    time[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if time[now] < dist:
            continue

        for j in graph[now]:
            cost = dist + j[1]

            if cost < time[j[0]]:
                time[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(start)

wasted_time = 0
for x in time:
    if wasted_time < x < INF:
        wasted_time = x

# 0도아니고, INF 도 아니면 수신은 한 것.

cnt = 0
for x in time:
    if x != INF and x != 0:
        cnt += 1

print(cnt, wasted_time)