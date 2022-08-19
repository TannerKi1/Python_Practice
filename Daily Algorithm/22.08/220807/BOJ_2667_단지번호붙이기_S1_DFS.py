N = int(input())
import sys
sys.setrecursionlimit(10000)

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

houses = []
house = 0

def dfs(x, y):
    global house # 글로벌 house를 가져오겠다.
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 2
        house += 1

        dfs(x+1, y) # 1, 1

        dfs(x, y+1) # 0, 2

        dfs(x, y-1) # 0, -1 False

        dfs(x-1, y) # -1, 1 False

        return True
    return False

check = []
cnt = 0
for m in range(N):
    for n in range(N):
        if dfs(m, n):
            cnt += 1
            houses.append(house) # 한 묶음이 끝날 때, 리스트에 개수를 append 하겠다.
            house = 0 # 다시 0부터 세어야하니까 house 초기화해줌.
            check.append((m, n))


print(cnt)
houses.sort()
for x in houses:
    print(x)

