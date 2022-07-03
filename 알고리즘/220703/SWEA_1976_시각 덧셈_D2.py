
T = int(input())


for x in range(1, T+1):
    b = list(map(int, input().split()))
    # b[0] 1번째 시간
    # b[1] 1번째 분
    # b[2] 2번째 시간
    # b[3] 2번째 분
    h = b[0] + b[2]
    m = b[1] + b[3]
    if m >= 60:
        m = m - 60
        h = h + 1
    if h >= 13:
        h = h - 12
    print(f'#{x} {h} {m}')