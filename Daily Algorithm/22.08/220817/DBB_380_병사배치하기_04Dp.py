# dp 풀이


# 리트코드 풀이
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

sub = []

for num in arr:
    i = bisect_left(sub, num)

    if i == len(sub):
        sub.append(num)

    else:
        sub[i] = num

print(len(sub))

