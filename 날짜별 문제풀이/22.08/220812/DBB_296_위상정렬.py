from collections import deque

V, E = map(int, input().split())

received = [0] * (V+1)

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    received[b] += 1
    graph[a].append(b)


def topology_sort():
    order = []
    q = deque([])

    for x in range(1, V+1):
        if received[x] == 0:
            q.append(x)

    ## 요까지는 구현 완료

    while q:
        now = q.popleft()
        order.append(now)

        for i in graph[now]:
            received[i] -= 1

            if received[i] == 0:
                q.append(i)

    for i in order:
        print(i, end = ' ')

topology_sort()

