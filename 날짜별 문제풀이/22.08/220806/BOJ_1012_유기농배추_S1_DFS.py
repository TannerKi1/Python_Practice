import sys
sys.setrecursionlimit(10000)
T = int(input())


for tc in range(T):
    M, N, K = map(int, input().split())
    # M 가로, N 세로

    graph = [[0] * M for _ in range(N)]

    def dfs(x, y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return False

        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            return True
        else:
            return False

    for _ in range(K):
        n, m = map(int, input().split())
        graph[m][n] = 1  # 가로세로가 뒤집어 지게 된다.

    result = 0
    for x in range(N):
        for y in range(M):
            if dfs(x, y):
                result += 1

    print(result)
