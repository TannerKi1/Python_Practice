T = int(input())


for i in range(1, T+1):
    N = list(map(int, input().split()))
    len_list = N[0]
    c_range = N[1]
    arr = list(map(int, input().split()))
    tray = []
    for k in range(0, len(arr)+1):
        tray.append(sum(arr[k:k+c_range]))
        if k + c_range == len(arr):
            break

    max_a = max(tray)
    min_a = min(tray)
    print(f'#{i} {max_a - min_a}')
