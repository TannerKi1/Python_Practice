C = int(input())

for x in range(C):
    score = list(map(int, input().split()))
    N = score[0]
    N_rscore = score[1::]
    N_sum = sum(score[1::])
    N_avg = N_sum / N
    count = 0

    for j in N_rscore:

        if j > N_avg:
            count += 1
        else:
            continue
    answer = count / N * 100

    print(f'{round(answer, 3):.3f}%')