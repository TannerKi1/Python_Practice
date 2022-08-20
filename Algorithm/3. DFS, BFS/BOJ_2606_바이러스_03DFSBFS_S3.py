import sys
input = sys.stdin.readline

n = int(input())
v = int(input())

# 간선 정보를 담을 그래프 틀 만들기
graph = [[] for _ in range(n + 1)]

# 방문 여부를 체크하는 리스트 만들기
visited = [False] * (n + 1)

# 간선 정보 받아오기 # 양방향으로 받아와야함
for i in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start, graph, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, graph, visited)


dfs(1, graph, visited)

# 감염 여부를 세는 곳
cnt = 0
for computer in visited:
    if computer:
        cnt += 1

# 자기 자신을 빼야 하므로
print(cnt - 1)
