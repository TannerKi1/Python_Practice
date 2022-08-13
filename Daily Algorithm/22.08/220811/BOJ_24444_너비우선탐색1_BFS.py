from collections import deque
import sys
input = sys.stdin.readline

V, E, start = map(int, input().split())

graph = [ [] for _ in range(V + 1)]
visited = [False] * (V + 1)


for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, V + 1):
    graph[i].sort()

count = [0] * (V + 1)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    cnt = 0

    while q:
        i = q.popleft()
        cnt += 1
        count[i] = cnt

        for x in graph[i]:
            if not visited[x]:
                visited[x] = True
                q.append(x)


bfs(start)

for x in range(1, V+1):
    print(count[x])

