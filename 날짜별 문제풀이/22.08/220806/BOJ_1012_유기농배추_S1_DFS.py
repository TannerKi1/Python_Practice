T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())

# M 가로, N 세로

graph = [[0] * M for _ in range(N)]

for _ in range(K):
    m, n = map(int, input().split())
    graph[n][m] = 1  # 가로세로가 뒤집어 지게 된다.

print(graph)


