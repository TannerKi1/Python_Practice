from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    j, k = map(int, input().split())
    graph[j].append(k)
    graph[k].append(j)

for i in range(len(graph)):
    graph[i].sort()


# print(graph) 여기까지 노드는 구현완료함.
# 내부 그래프를 다시 sort해줘야 오름차순으로 방문할 수 있게 됨.

# DFS부터 구현해보기 (재귀함수로)
def dfs(graph, V, visited_d):
    if not visited_d[V]:
        visited_d[V] = True
        print(V, end=' ')

        for i in graph[V]:
            if not visited_d[i]:
                dfs(graph, i, visited_d)


visited_d = [False] * (N + 1)

dfs(graph, V, visited_d)
print()


# BFS 구현해 보기 (덱으로)
def bfs(graph, V, visited_b):
    queue = deque([V])
    visited_b[V] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]: # popleft를 하면서 이 친구의 연결된 다른 노드를 가져오는 것. 아까는 V로 고정되어있었으니, 3, 1, 4에서 끝났던 것
            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = True


visited_b = [False] * (N + 1)

bfs(graph, V, visited_b)
