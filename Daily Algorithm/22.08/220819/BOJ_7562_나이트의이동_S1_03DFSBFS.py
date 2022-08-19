from collections import deque

dx = [+2, +1, -1, -2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]



def knight_move(x, y, sx, sy):

    queue = deque()
    queue.append((x, y))

    while queue:
        curX, curY = queue.popleft()
        if curX == sx and curY == sy:
            print(graph[curX][curY] - 1)
            return True

        for i in range(8):
            nx = curX + dx[i]
            ny = curY + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[curX][curY] + 1
                queue.append((nx, ny))
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    graph = [[0] * N for _ in range(N)]
    x, y = map(int, input().split())
    sx, sy = map(int, input().split())
    graph[x][y] = 1
    knight_move(x, y, sx, sy)




