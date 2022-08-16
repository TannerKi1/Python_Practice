from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j)) # 시간 0이 들어가는게 포인트.


data.sort()  # 바이러스를 오름차순 정렬

q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    # print(q) # 실제 queue가 어떻게 구동되는지 확인가능한 장치
    virus, s, x, y = q.popleft() # 이 장치가 있어서 초 관계없이 무한히 커지는 걸 막을 수 있다.?
    # 아까는 for문이어서 다음 바이러스로 끊어줄 장치가 없었음. 그렇다고 시간 카운트가 들어간 것도 아니었고.
    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, s+1, nx, ny))



print(graph[target_x - 1][target_y - 1])

