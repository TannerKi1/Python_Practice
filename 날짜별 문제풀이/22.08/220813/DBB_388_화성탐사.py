N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

for k in range(N):
    for a in range(N):
        for b in range(N):
            