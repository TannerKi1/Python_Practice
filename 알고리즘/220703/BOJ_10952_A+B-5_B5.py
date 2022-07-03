import sys
switch = 1

while switch == 1:
    N = list(map(int, sys.stdin.readline().split()))
    if N[0] == 0:
        switch = 0
    else:
        print(N[0] + N[1])



# while을 이용한 방법
# 사실 T값이 없기 때문에 range로 돌리면 언제 멈춰야할 지 알 수가 없음.