T = int(input())
from collections import deque

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = []

    for _ in range(V+1):
        graph.append([])

    for _ in range(E):
        m, j = map(int, input().split())
        graph[m].append(j)
        graph[j].append(m)

    s, g = map(int, input().split())

    # 기본 정보는 다 받은 상태.

    visited = [False] * (V + 1)

    def bfs(graph, start, visited):
        queue = deque([(start, 0)])
        visited[start] = True

        while queue:
            p, cnt = queue.popleft()

            for j in graph[p]:
                if not visited[j] and j == g:
                    return cnt + 1 # 튜플로 묶어서 정보를 저장해준다.
                elif not visited[j]:
                    visited[j] = True
                    queue.append((j, cnt + 1)) # 이 경우, 3과 4는 (3, 1) (4, 1)로 저장되게 된다.

        return 0

    print(f'#{tc}', end = ' ')
    print(bfs(graph, s, visited))



