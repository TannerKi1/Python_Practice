n = int(input())
arr = []

for i in range(n):
    t = list(map(int, input().split()))
    arr.append(t)

# 여기까지 삼각형은 빠르게 받았습니다.


if n == 1:
    print(arr[0][0])

if n == 2:
    print(max(arr[0][0] + arr[1][0], arr[0][0] + arr[1][1]))


if n >= 3:

    d = []
    d.append([arr[0][0]])
    d.append([arr[0][0] + arr[1][0], arr[0][0] + arr[1][1]])

    for i in range(2, n):
        t = list()
        t.append(d[i-1][0] + arr[i][0])
        for j in range(1, i):
            t.append(max(d[i-1][j-1] + arr[i][j], d[i-1][j] + arr[i][j]))
        t.append(d[i-1][-1] + arr[i][-1])
        d.append(t)

    max_num = 0

    for x in d[n-1]:
        if x > max_num:
            max_num = x

    print(max_num)


print(d)