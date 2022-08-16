N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

result = []
down = len(stages)

for i in range(1, N+1):

    count = stages.count(i)
    if down == 0:
        count = 0

    fail = count / down
    result.append((i, fail))

    down -= count

result.sort(key = lambda x: x[1], reverse = True)

answer = [i[0] for i in result]

print(answer)




