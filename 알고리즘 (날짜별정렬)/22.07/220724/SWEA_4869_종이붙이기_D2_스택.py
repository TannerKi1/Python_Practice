TC = int(input())

for tc in range(TC):
    d = [0]
    d.append(1)
    d.append(3)

    n = int(input()) // 10

    if n == 1:
        print(1)
        exit()

    if n == 2:
        print(3)
        exit()

    for i in range(3, n+1):
        d.append(d[i-1] + 2 * d[i-2])

    print(f'#{tc+1} {d[n]}')


# 굿