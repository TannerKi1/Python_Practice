from copy import deepcopy
from itertools import combinations
from collections import deque

n, m = map(int, input().split())
Map = []

for _ in range(n):
    Map.append(list(map(int, input().split())))

wall = []
virus = []
for i in range(n):
    for j in range(m):
        if Map[i][j] == 2:
            virus.append((i, j))
        if Map[i][j] == 0:
            wall.append((i, j))


def bfs(Map):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    for z in range(len(virus)):
        q.append(virus[z])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and Map[nx][ny] == 0:
                Map[nx][ny] = 2
                q.append((nx, ny))

    return Map

def count(Map):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1

    return cnt


Wall_list = list(combinations(wall, 3))

max_val = 0

for i in range(len(Wall_list)):
    temp = deepcopy(Map)
    for j in range(3):
        temp[Wall_list[i][j][0]][Wall_list[i][j][1]] = 1

    temp = bfs(temp)
    val = count(temp)
    max_val = max(max_val, val)

print(max_val)







