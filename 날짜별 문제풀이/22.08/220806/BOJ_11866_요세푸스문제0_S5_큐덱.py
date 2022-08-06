from collections import deque

N, K = map(int, input().split())

arr = [_ for _ in range(1, N+1)]

n_arr = deque(arr)
case = []
while len(n_arr) > 0:
    n_arr.rotate(-(K-1))
    case.append(n_arr.popleft())

print("<", end='')
for i in range(N-1):
    print(case[i], end=', ')
print(case[N-1], end='')
print(">")


# deque 에는 rotate라는 명령어가 있다.
