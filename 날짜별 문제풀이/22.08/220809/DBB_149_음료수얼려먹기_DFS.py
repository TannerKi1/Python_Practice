# 3회차 다시 풀기

n, m = map(int, input().split())
graph = []

for x in range(n):
    graph.append(list(map(int, input())))

# 그래프 초기화 완료

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: # 조건을 벗어나는 경우는 컷!
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    else:
        return False


cnt = 0
for x in range(n):
    for y in range(m):
        if dfs(x, y):
            cnt += 1
        else:
            cnt += 0

print(cnt)

