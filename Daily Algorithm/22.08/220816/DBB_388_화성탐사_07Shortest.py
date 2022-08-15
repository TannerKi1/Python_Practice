# 1칸씩 이동...
# 넓이우선 탐색? -> 덱? 다익스트라(비용이 나오니까)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

T = int(input())



for _ in range(T):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    distance = [[INF] * (N) for _ in range(N)]
    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[0][0] = graph[0][0]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[N-1][N-1])




