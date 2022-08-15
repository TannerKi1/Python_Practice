N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

length = len(stages)

answer = []

for i in range(1, N+1):
    count = stages.count(i)

    if length == 0:
        fail = 0

    fail = count / length
    answer.append((i, fail))

    length -= count

answer.sort(key = lambda x: x[1], reverse = True)

answer = [i[0] for i in answer] # 이렇게 리스트 깔끔하게 처리하는 것도 가능...

print(answer)





