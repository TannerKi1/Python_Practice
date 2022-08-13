from collections import deque

V = int(input())
E = int(input())
graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, visited, start):

    dq = deque()
    dq.append(start)
    visited[start] = True

    while dq:
        k = dq.popleft()
        print(k, end=' ')

        for i in graph[k]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)

bfs(graph, visited, 1)




