import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [ [] for _ in range(n+1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: # 우선순위라고 뽑아줬는데, 뽑은 값이 기존 값보다 크면 무시 (갱신이 되었다 -> 이미 방문했다)
            continue

        for i in graph[now]: #방문을 하지 않은 경우에...
            cost = dist + i[1] #갱신가능한 후보는 이 값을 가집니다.

            if cost < distance[i[0]]: # 이걸 현재 상태랑 비교를 해서, 후보가 현재 값보다 작다면
                distance[i[0]] = cost #외부 준거 거리를 최신화 시켜주고
                heapq.heappush(q, (cost, i[0])) # 해당 거리와 노드 번호를 heapq에 밀어줍니다.

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])