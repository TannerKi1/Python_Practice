TC = int(input())

for tc in range(TC):
    V, E = map(int, input().split())
    graph = []

    for _ in range(V + 1):
        graph.append([])

    for _ in range(E):
        m, n = map(int, input().split())
        graph[m].append(n)  # 이 문제에서는 단방향과 양방향을 구분함.

    p, q = map(int, input().split())

    visited = [False] * (V + 1)

    answer = list()


    def dfs(graph, v, visited):
        visited[v] = True
        answer.append(v)
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

        if q in answer:
            return 1
        else:
            return 0


    print(f'#{tc + 1}', end=' ')
    print(dfs(graph, p, visited))
