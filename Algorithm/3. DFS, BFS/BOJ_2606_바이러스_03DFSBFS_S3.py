# 컴퓨터 개수와 간선 개수 입력
v = int(input())
e = int(input())

# 컴퓨터 연결 상태를 저장할 그래프 생성
graph = [[] for _ in range(v + 1)]

# e만큼 돌면서 입력
for _ in range(e):
    a, b = map(int, input().split())

    # 양방향이기 때문에 양쪽으로 입력
    graph[a].append(b)
    graph[b].append(a)

#방문이 기록가능한 방문 노드 만들기
visited = [0] * (v + 1)


# dfs 만들기
def dfs(v):

    visited[v] = 1

    for new in graph[v]:
        if visited[new] == 0:
            dfs(new)


# dfs 실행하기
dfs(1)

# 전체 방문 횟수 카운팅하기
cnt = 0
for i in range(2, v+1):
    if visited[i] == 1:
        cnt += 1

print(cnt)
print(visited)