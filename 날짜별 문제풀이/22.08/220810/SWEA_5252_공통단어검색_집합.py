T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    a = set()
    b = set()
    for _ in range(A):
        a.add(input())

    for _ in range(B):
        b.add(input())

    c = a & b
    print(f'#{tc} {len(c)}')
