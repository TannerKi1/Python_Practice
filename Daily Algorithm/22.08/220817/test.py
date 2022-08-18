N = int(input())
graph = [[] for _ in range(N+1)]

TC = int(input())

for _ in range(TC):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


dfs(1)

print(visited.count(True) - 1)

