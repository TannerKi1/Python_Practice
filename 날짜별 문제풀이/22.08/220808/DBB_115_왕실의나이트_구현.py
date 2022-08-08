
# 8가지 방향을 기록

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

k = input()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] #ord값으로 처리해서 숫자로 바꿀 수도 있었음.

x = int(k[1])
y = alpha.index(k[0])

cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or nx > 8 or ny < 0 or ny > 7:
        continue

    cnt += 1

print(cnt)