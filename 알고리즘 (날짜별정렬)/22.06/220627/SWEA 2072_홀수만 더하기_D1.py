
T = int(input())
for i in range(1, T+1):
    a = list(map(int, input().split()))

    b = []
    for j in a:
        if j % 2 != 0:
            b.append(j)

    print(f'#{i} {sum(b)}')

## list 컴프리헨션으로 풀기 가능?

# 생각해보자고...