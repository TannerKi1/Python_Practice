

TC = int(input())

for tc in range(1, TC+1):
    arr = []
    N, M = map(int, input().split())
    for _ in range(N):
        arr.append(input())

    for i in range(0, N):
        for j in range(0, N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                print(f'#{tc} {arr[i][j:j+M]}')
                break


    new_arr = []
    for i in range(0, N):
        arr_column = []
        for j in range(0, N):
            arr_column.append(arr[j][i])
        new_arr.append(arr_column)

    switch = True
    for i in range(0, N):
        for j in range(0, N - M + 1):
            if new_arr[i][j:j+M] == new_arr[i][j:j+M][::-1]:
                print(f"#{tc} {''.join(new_arr[i][j:j+M])}")
                break





