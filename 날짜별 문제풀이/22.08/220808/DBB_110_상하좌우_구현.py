N = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
command = ['U', 'D', 'L', 'R'] # 굳이 2*2 그래프를 만들 필요도 없었음. 그냥 좌표는 숫자로 주어지니까.

x, y = 1, 1

plans = input().split()  #map이 아니면 굳이 앞에 list로 닫아줄 필요 없음.

for plan in plans:
    for i in range(4):
        if plan == command[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue

    x, y = nx, ny

print(x, y)















