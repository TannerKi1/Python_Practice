import sys
from collections import deque
N = int(sys.stdin.readline())

d_arr = deque([i for i in range(1, N+1)])

for _ in range(N-1):
    d_arr.popleft()
    d_arr.rotate(-1)

for x in d_arr:
    print(x)
