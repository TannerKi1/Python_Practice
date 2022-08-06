T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_2 = [(val, idx) for idx, val in enumerate(arr)]
    cnt = 0 # cnt 위치 신경쓰기

    while True:
        if arr_2[0][0] == max(arr_2, key = lambda x : x[0])[0]:
            cnt += 1 # 어쨌거나 최대값이니까 인쇄는 해야함.
            if arr_2[0][1] == m:
                print(cnt)
                break
            else:
                b = arr_2.pop(0)

        else:
            b = arr_2.pop(0)
            arr_2.append(b)


