import sys
from collections import deque
N = int(sys.stdin.readline())

n_list = list(map(int, sys.stdin.readline().split()))
n2_list = []
stack = []
ans = [-1] * N

idx = 0
for i in range(len(n_list)):
    n2_list.append((n_list[i], idx))
    idx += 1

n2_list_r = n2_list[::-1]


while len(n2_list_r) > 1:
    tmp, idx = n2_list_r.pop()
    stack.append((tmp, idx))

    while stack and n2_list_r[-1][0] > stack[-1][0]:
        tmp, idx = stack.pop()
        ans[idx] = n2_list_r[-1][0]

    # 만약에 빈칸이거나, 왼쪽 값이 스택 값보다 작으면 무시되고 다시 한 칸이 올라간다.

print(*ans)




