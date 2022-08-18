from itertools import combinations

n, m = map(int, input().split())
array = list(map(int, input().split()))

balls = list(combinations(array, 2))

cnt = 0
for x in balls:
    a, b = x
    if a != b:
        cnt += 1

print(cnt)
