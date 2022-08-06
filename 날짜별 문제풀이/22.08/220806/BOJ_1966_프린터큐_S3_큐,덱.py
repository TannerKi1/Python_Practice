import sys
from collections import deque
t = int(sys.stdin.readline())

for tc in range(t):
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, input().split()))

    arr_2 = deque(arr)
    if arr_2[0] < max(arr_2):
        arr_2.rotate(-1)
    elif arr_2[0] >= max(arr_2):
        arr_2.popleft()


# enumerate로 같은 숫자일 경우에는 첫 숫자로 구분을 해줘야할까?



