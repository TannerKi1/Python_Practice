import sys

N = int(input())
empty_arr = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    empty_arr.append((x, y))

empty_arr.sort(key = lambda x : x[1])
empty_arr.sort(key = lambda x : x[0])


for x, y in empty_arr:
    print(x, y)
