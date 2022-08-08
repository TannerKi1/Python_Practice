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
    # 위에서 범위를 초과한 값이 나왔다면 아래 continue에 걸려서 무시된 다음, 0단계로 돌아가 다음 plan을 돌게 된다
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue # pass로 한다면 9 1이 되는 걸 알 수 있다. continue는 조건에 맞지 않으면 반영 없이 원래 for문으로 초기화됨

    # 만약 범위에 걸리지 않았다면, x와 y는 범위에 맞는 nx 와 ny의 값으로 초기화되게 된다.
    x, y = nx, ny

print(x, y)















