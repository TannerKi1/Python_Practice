import sys
from collections import deque

input = sys.stdin.readline
v, e, start = map(int, input().split())

# 정점 정보를 담을 그래프
graph = [[] for _ in range(v + 1)]

# 방문 정보를 담을 리스트 (딥카피로 복제해서 사용하는 것도 가능하겠지만 편의상 2개로 만들겠음)
d_visited = [False] * (v + 1)
b_visited = [False] * (v + 1)

# 각각 간선 연결 상태를 정점 그래프에 연결해준다.
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 간선 연결 상태를 오름차순으로 구현해준다.
for i in range(1, v + 1):
    graph[i].sort()


# dfs 함수 구현
def dfs(v, d_visited, graph):
    d_visited[v] = True # 맨 처음 들어오는 애를 처리해주기 위한 문장
    print(v, end=' ')

    for key in graph[v]:
        if not d_visited[key]:
            d_visited[key] = True
            dfs(key, d_visited, graph)


# bfs 함수 구현
def bfs(start, b_visited, graph):
    b_visited[start] = True

    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()
        print(x, end=' ')

        for i in graph[x]:
            if not b_visited[i]:
                b_visited[i] = True
                queue.append(i)


# dfs 시동
dfs(start, d_visited, graph)
print()

# bfs 시동
bfs(start, b_visited, graph)
