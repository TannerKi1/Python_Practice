# 그냥 리스트로 풀자


T = int(input())
for i in range(T):
    N = int(input())
    count = [0] * 10
    number = str(input())

    for x in number:
        count[int(x)] += 1

    max_Count = 0
    idx = []
    for k in range(len(count)):   # N은 4까지 비교됨
        if count[k] >= max_Count:
            max_Count = count[k]
            idx.append(k)

    print(f'#{i+1} {idx[-1]} {max_Count}')







