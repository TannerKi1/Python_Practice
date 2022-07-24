T = int(input())

for tc in range(T):
    picture = [[0] * 10 for _ in range(10)]
    n = int(input())
    count = 0
    for _ in range(n):
        small_arr = list(map(int, input().split()))
        a = small_arr[0]
        b = small_arr[1]
        c = small_arr[2]
        d = small_arr[3]
        color = small_arr[4]
        for i in range(a, c+1):
            for j in range(b, d+1):
                picture[i][j] = picture[i][j] + color

    for z in range(10):
        for y in range(10):
            if picture[z][y] == 3:
                count += 1

    print(f'#{tc+1} {count}')



