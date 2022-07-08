T = int(input())
for x in range(T):
    arr = list(map(str, input().split('X')))
    arr_2 = []
    for j in arr:
        arr_2.append(j.count('O'))

    real_answer = []

    for n in arr_2:
        real_answer.append(int(n * (n+1) / 2))

    print(sum(real_answer))




