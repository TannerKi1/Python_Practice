import heapq
INF = int(1e9)


N, M, K, X = map(int, input().split())

distance = [INF] * (N+1)

graph = [ [] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))


q = []
heapq.heappush(q, (0, X))
distance[X] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for item in graph[now]:
        cost = dist + item[1]

        if cost < distance[item[0]]:
            distance[item[0]] = cost
            heapq.heappush(q, (cost, item[0]))

answer = []
for i in range(1, N+1):
    if distance[i] == K:
        answer.append(i)

if len(answer) >= 1:
    for x in answer:
        print(x)

if len(answer) == 0:
    print(-1)



