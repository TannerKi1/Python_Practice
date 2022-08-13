from collections import deque
N, E, start = map(int, input().split())

visited = [False] * (N+1)

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort(reverse = True)


order = [0] * (N+1)

def bfs(start):
    q = deque([start])
    visited[start] = True

    cnt = 0

    while q:
        k = q.popleft()
        cnt += 1
        order[k] = cnt
        for x in graph[k]:
            if not visited[x]:
                q.append(x)
                visited[x] = True

bfs(start)

for i in range(1, N+1):
    print(order[i])

