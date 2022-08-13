import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V, E, start = map(int, input().split())

visited = [False] * (V + 1)
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(V + 1):
    graph[i].sort()

cnt = 1

answer = [0] * (V + 1)
def dfs(start):
    global cnt
    visited[start] = True
    answer[start] = cnt

    for j in graph[start]:
        if not visited[j]:
            cnt += 1
            dfs(j)

dfs(start)

for i in range(1, V + 1):
    print(answer[i])