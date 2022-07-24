T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr_small = []
        k = input()
        for z in range(N):
            arr_small.append(k[z])
        arr.append(arr_small)

## 여기까지 쪼개서 리스트로 받는 거 성공.

    res_list = []
    for x in range(N):
        res = ''
        for j in range(N):
            res += arr[x][j]

        res_list.append(res)

    for x in range(N):
        res = ''
        for j in range(N):
            res += arr[j][x]

        res_list.append(res)

# 중간부터 세는 건 어떻게 해야할 지 좀 더 생각해보기






