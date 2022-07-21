T = int(input())

for x in range(T):
    k = int(input())

    dp_0 = [1, 0, 1]

    for i in range(3, k+2):
        dp_0.append(dp_0[i-1] + dp_0[i-2])

    dp_1 = [0, 1, 1]

    for i in range(3, k+2):
        dp_1.append(dp_1[i-1] + dp_1[i-2])

    print(dp_0[k], dp_1[k])


# 저장을 했다가 부르게 된다.

# 일반적인 재귀함수로 하면 f(0)과 f(1)이 계속해서 반복호출되게 됨.