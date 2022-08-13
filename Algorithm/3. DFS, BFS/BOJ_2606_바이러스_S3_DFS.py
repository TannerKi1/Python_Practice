N = int(input())  # 이차원 리스트가 만들어지는 개수
TC = int(input())  # 연결되어 있는 정보가 제공되는 횟수

graph = [[] for _ in range(N + 1)]

for _ in range(TC):
    j, k = map(int, input().split())
    graph[j].append(k)
    graph[k].append(j)

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False] * (N + 1)

dfs(graph, 1, visited)

print((visited.count(True)) - 1)