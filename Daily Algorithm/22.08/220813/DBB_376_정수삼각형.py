N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

d = [[arr[0][0]],
     [arr[0][0] + arr[1][0], arr[0][0] + arr[1][1]]
     ]

for i in range(2, N):
    t = []
    t.append(d[i-1][0] + arr[i][0])
    for j in range(1, i):
        t.append(max(d[i-1][j-1] + arr[i][j], d[i-1][j] + arr[i][j]))
    t.append(d[i-1][-1] + arr[i][-1])
    d.append(t)


print(d)


