n = int(input())
graph = []
house = 0
import sys
sys.setrecursionlimit(10000)

# 단지 맵 그리기 완료
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    global house

    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 2
        house += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

houses = []
cnt = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            houses.append(house)
            house = 0
            cnt += 1

print(cnt)
houses.sort()
for x in houses:
    print(x)




