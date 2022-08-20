from collections import deque
import sys
input = sys.stdin.readline


def bfs(sx, sy):

    queue = deque()
    queue.append((sx, sy))

    while queue:
        ax, ay = queue.popleft()

        dh = [1, -1, 0, 0]
        dw = [0, 0, -1, 1]

        for i in range(4):
            nh = ax + dh[i]
            nw = ay + dw[i]

            if 0 <= nh < h and 0 <= nw < w and graph[nh][nw] == 1:
                graph[nh][nw] = 0
                queue.append((nh, nw))


T = int(input())

for _ in range(T):
    w, h, k = map(int, input().split())

    graph = [[0] * w for _ in range(h)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                graph[i][j] = 0
                bfs(i, j)
                cnt += 1

    print(cnt)







