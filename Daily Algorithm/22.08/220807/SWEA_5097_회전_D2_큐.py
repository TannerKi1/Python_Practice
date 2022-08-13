T = int(input())
from collections import deque

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))

    mod = M % N

    arr.rotate(-mod)
    print(f'#{tc} {arr[0]}')

