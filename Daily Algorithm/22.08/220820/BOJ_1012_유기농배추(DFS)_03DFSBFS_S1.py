import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)
# dfs 함수 만들기
def dfs(x, y):

    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 2 # 이걸해야 다른 좌표값이 또 1로 들어가 True나오는 걸 막을 수 있음.
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


# 테스트 케이스 돌리기
T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    # 가로길이가 m, 세로길이가 n 인 상황

    cnt = 0

    # 그래프 그리기 완성
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    # dfs 돌려보기
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                cnt += 1

    print(cnt)





