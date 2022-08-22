# 문제를 보고 BFS일 것 같으면 바로 적용시켜주기
from collections import deque

# 도시의 개수, 간선 개수, 목표 거리, 시작점
n, m, k, start = map(int, input().split())

# 단방향 도로인 것을 조심
# 연결하는 그래프 틀 만들고, 간선정보 채워넣기
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)

# 방문정보를 기록할 리스트 만들기
visited = [-1] * (n + 1)

# BFS로 풀어야하기 때문에 deque을 맨 위에 import 해준다.


def bfs(inputX):
    queue = deque()
    queue.append(start)

    # 가장 시작점의 방문점은 1로 처리
    visited[start] = 0

    while queue:
        now = queue.popleft()

        for x in graph[now]:
            # 만약 방문하지 않은 도시라면, 현재 방문거리에서 1을 더해준다.
            if visited[x] == -1:
                visited[x] = visited[now] + 1
                # 그리고 덱에 해당 도시의 정보를 넣어준다.
                queue.append(x)


# bfs 실행
bfs(start)

# 스위치를 만들면 따로 리스트를 만들지 않고도 없는 경우를 구분할 수 있다.
check = False

# for문 돌면서 방문거리 K와 일치하는 도시 번호 뽑기

# 시작점을 0으로 잡고, 방문하지 않음을 -1로 만들면 k를 깔끔하게 뽑을 수 있다.
for i in range(1, n+1):
    if visited[i] == k:
        print(i, end=' ')
        check = True

# True 스위치가 바뀌지 않았다면 -1만 나오게 된다.
if not check:
    print(-1)










