import sys
M = int(input())
S = set()


for x in range(M):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == 'all':
            S = set([i for i in range(1, 21)])

        else:
            S = set()

    else:
        order, x = temp[0], int(temp[1])
        if order == 'add':
            S.add(x)
        elif order == 'remove':
            S.discard(x)
        elif order == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
        elif order == 'check':
            if x in S:
                print(1)
            else:
                print(0)


# 집합 함수의 명령 remove와 discard의 차이 이해하기
# int와 str 가 다르면 답이 안 나올 수 있다.