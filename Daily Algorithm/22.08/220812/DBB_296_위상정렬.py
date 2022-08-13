from collections import deque

V, E = map(int, input().split())

visited_checker = [0] * (V+1)

graph = [ [] for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    visited_checker[b] += 1
    graph[a].append(b)

visit = []

q = deque()

for i in range(1, V+1):
    if visited_checker[i] == 0:
        q.append(i)

# while indent 위치 조심.

while q:
    now = q.popleft()
    visit.append(now)

    for j in graph[now]:
        visited_checker[j] -= 1
        if visited_checker[j] == 0:
            q.append(j)

print(visit)
