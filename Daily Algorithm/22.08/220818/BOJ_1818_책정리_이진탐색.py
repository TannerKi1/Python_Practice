from bisect import bisect_left

N = int(input())
array = list(map(int, input().split()))

answer = []

for x in array:
    if bisect_left(answer, x) == len(answer):
        answer.append(x)

    else:
        answer[bisect_left(answer, x)] = x

print(len(answer))

