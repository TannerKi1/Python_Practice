

n, m = map(int, input().split()) # 바다 지도용
x, y, direction = map(int, input().split()) # 현재 위치, 바라보는 방향 받기
# 방문을 체크하기 위한 [0]리스트 만들기
d = [[0] * m for _ in range(n)]  # 세로크기가 뒤에 range로 들어가야함.
d[x][y] = 1 # 랜딩하는 순간 이미 체크

# 바다, 육지 지도를 받기
arr = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서 순으로 만들었음.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 도는 장치 만들기, 여기서는 함수로 구현함
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
# turn_left가 1번 선언 될 때마다 왼쪽으로 도는데, 북(0), 서(3), 남(2), 동(1) 순으로 바라봄
# 음수 값이면 3으로 바꿔서 계속 돌게 됨.

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue # 조건만 맞다면 아래 else로 빠지지 않고 turn_time 0을 유지한 채 가능
    else: # 이미 갔던곳이거나 바다를 만나면 한번 돌게 된다.
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction] # 원상태로 돌았으니까 뒤로 돌아가게 된다.
        ny = y - dy[direction]

        if arr[nx][ny] == 0:
            x = nx
            y = ny

        else: # 뒤가 다 바다인 경우
            break #while 문 탈출
        turn_time = 0

print(count)


