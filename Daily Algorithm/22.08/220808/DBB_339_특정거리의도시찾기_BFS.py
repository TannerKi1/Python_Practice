from collections import deque
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]


for _ in range(M):
    j, k = map(int, input().split())
    graph[j].append(k)

visited = [False] * (N + 1)
answer = []

def bfs(graph, X, visited):
    queue = deque([(X, 0)])
    visited[X] = True

    while queue:
        (k, j) = queue.popleft()
        answer.append((k, j))

        for i in graph[k]:
            if not visited[i]:
                queue.append((i, j+1))
                visited[i] = True


bfs(graph, X, visited)

# 아래를 더 깔끔하게 할 수는 없을지...?

arr = []
for x in answer:
    if x[1] == K:
        arr.append(x[0])

if len(arr) >= 1:
    for k in arr:
        print(k)

if len(arr) == 0:
    print(-1)






