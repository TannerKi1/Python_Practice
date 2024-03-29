n, m = map(int, input().split())
data = []
temp = [ [0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0

def virus(x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def score_count():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # for i in range(n):
        #     for j in range(m):
        #         print(temp[i][j], end = ' ')
        #     print()

        result = max(result, score_count())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                for a in range(n):
                    for b in range(m):
                        print(data[a][b], end=' ')
                    print()
                print("---")
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)


