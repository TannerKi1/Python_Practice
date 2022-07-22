
# 목표 : N의 숫자가 주어지면 N까지 홀수는 -로, 짝수는 +로 리턴해서 더하기

T = int(input())

for x in range(1, T+1):
    b = int(input())
    C = 0
    for k in range(1, b+1):
        if k % 2 != 0:
            C += k
        elif k % 2 == 0:
            C -= k
    print(f'#{x} {C}')


# 글로벌 변수인지, for 안의 변수인지 잘 생각해주자. 완전 밖으로 빼게 되면 돌 때마다 값이 업데이트 되게 됨