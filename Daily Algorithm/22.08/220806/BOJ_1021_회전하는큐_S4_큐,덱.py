from collections import deque
N, M = map(int, input().split())
arr_2 = list(map(int, input().split()))

num_arr = [_ for _ in range(1, N+1)]
arr = deque(num_arr)

cnt = 0
for x in arr_2:
    if x == arr[0]:
        arr.popleft()

    else:
        l_rotate = -1
        r_rotate = 1

        for _ in range(N):
            arr.rotate(l_rotate)
            if arr[0] == x:
                break
            else:
                l_rotate -= 1

        for _ in range(N):
            arr.rotate(r_rotate)
            if arr[0] == x:
                break
            else:
                r_rotate += 1

        arr.rotate()

        cnt += min(abs(l_rotate), r_rotate)

print(cnt)