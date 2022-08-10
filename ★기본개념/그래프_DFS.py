V = int(input())
E = int(input())

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(start):

    visited[start] = True
    print(start, end = ' ')

    for x in graph[start]:
        if not visited[x]:
            visited[x] = True
            dfs(x)


dfs(1)





