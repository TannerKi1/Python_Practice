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

    # 범위를 벗어나는 경우에는 False돌려주고 재귀 탈출하기
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 2
        house += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True # 재귀들을 끝까지 다 돌고 True값을 들고 탈출 이미 그래프값의 숫자는 변형됨.
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




