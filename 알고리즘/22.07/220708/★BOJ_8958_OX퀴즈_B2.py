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

# 맥에서 타이핑한 게 윈도우에서도 잘 보이는지 테스트



